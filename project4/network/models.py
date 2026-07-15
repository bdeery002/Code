from django.contrib.auth.models import AbstractUser
from django.db import models


# The default user model includes the following fields:
# UserName, password, email,first_name last_name

class User(AbstractUser):
    pass

# models.Model creates a database table for the Post model with the following fields:

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")

    def __str__(self):
        return f"{self.author} - {self.created_at:%Y-%m-%d %H:%M}"


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower} follows {self.following}"
