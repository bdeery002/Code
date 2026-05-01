from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
import json

from .models import User, Post, Follow


def index(request):
    posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "page_obj": page_obj
    })

@login_required
def following(request):
    # Get all users the current user follows
    followed_users = request.user.following.values_list("following", flat=True)
    posts = Post.objects.filter(author__in=followed_users).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "page_obj": page_obj
    })

def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, "network/profile.html", {
        "profile_user": profile_user,
        "page_obj": page_obj,
        "is_following": is_following,
        "followers_count": profile_user.followers.count(),
        "following_count": profile_user.following.count(),
    })

@login_required
@require_POST
def new_post(request):
    content = request.POST.get("content", "").strip()
    if content:
        Post.objects.create(author=request.user, content=content)
    return HttpResponseRedirect(reverse("index"))

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Security check - ensure user owns this post
    if post.author != request.user:
        return JsonResponse({"error": "Permission denied."}, status=403)

    if request.method == "PUT":
        data = json.loads(request.body)
        content = data.get("content", "").strip()
        if content:
            post.content = content
            post.save()
            return JsonResponse({"success": True, "content": post.content})
        return JsonResponse({"error": "Content cannot be empty."}, status=400)

    return JsonResponse({"error": "PUT request required."}, status=400)

@login_required
def toggle_like(request, post_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        "liked": liked,
        "like_count": post.likes.count()
    })

@login_required
@require_POST
def toggle_follow(request, username):
    profile_user = get_object_or_404(User, username=username)

    # Prevent self-following
    if profile_user == request.user:
        return JsonResponse({"error": "Cannot follow yourself."}, status=400)

    follow = Follow.objects.filter(follower=request.user, following=profile_user)

    if follow.exists():
        follow.delete()
        is_following = False
    else:
        Follow.objects.create(follower=request.user, following=profile_user)
        is_following = True

    return JsonResponse({
        "is_following": is_following,
        "followers_count": profile_user.followers.count()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
