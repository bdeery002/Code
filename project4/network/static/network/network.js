document.addEventListener('DOMContentLoaded', function() {

    // Handle like buttons
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            toggleLike(postId, this);
        });
    });

    // Handle edit buttons
    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.post-card');
            showEditArea(card);
        });
    });

    // Handle cancel buttons
    document.querySelectorAll('.cancel-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.post-card');
            hideEditArea(card);
        });
    });

    // Handle save buttons
    document.querySelectorAll('.save-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.post-card');
            savePost(card);
        });
    });

    // Handle follow/unfollow button (only exists on profile page)
    const followBtn = document.querySelector('#follow-btn');
    if (followBtn) {
        followBtn.addEventListener('click', function() {
            toggleFollow(this);
        });
    }

});


function toggleLike(postId, button) {
    fetch(`/posts/${postId}/like`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        // Update like count
        const card = button.closest('.post-card');
        card.querySelector('.like-count').textContent = data.like_count;

        // Toggle button style
        if (data.liked) {
            button.classList.remove('btn-outline-danger');
            button.classList.add('btn-danger');
        } else {
            button.classList.remove('btn-danger');
            button.classList.add('btn-outline-danger');
        }
    })
    .catch(error => console.error('Error:', error));
}


function showEditArea(card) {
    const content = card.querySelector('.post-content');
    const editArea = card.querySelector('.edit-area');
    const editBtn = card.querySelector('.edit-btn');
    const textarea = card.querySelector('.edit-textarea');

    // Populate textarea with current content
    textarea.value = content.textContent.trim();

    content.style.display = 'none';
    editBtn.style.display = 'none';
    editArea.style.display = 'block';
}


function hideEditArea(card) {
    const content = card.querySelector('.post-content');
    const editArea = card.querySelector('.edit-area');
    const editBtn = card.querySelector('.edit-btn');

    content.style.display = 'block';
    editBtn.style.display = 'inline-block';
    editArea.style.display = 'none';
}


function savePost(card) {
    const postId = card.dataset.postId;
    const textarea = card.querySelector('.edit-textarea');
    const newContent = textarea.value.trim();

    if (!newContent) {
        alert('Post content cannot be empty.');
        return;
    }

    fetch(`/posts/${postId}/edit`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ content: newContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        // Update the visible post content without reloading
        card.querySelector('.post-content').textContent = data.content;
        hideEditArea(card);
    })
    .catch(error => console.error('Error:', error));
}


function toggleFollow(button) {
    const username = button.dataset.username;

    fetch(`/profile/${username}/follow`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error(data.error);
            return;
        }
        // Update button text and style
        if (data.is_following) {
            button.textContent = 'Unfollow';
            button.classList.remove('btn-primary');
            button.classList.add('btn-outline-secondary');
        } else {
            button.textContent = 'Follow';
            button.classList.remove('btn-outline-secondary');
            button.classList.add('btn-primary');
        }
        // Update follower count
        document.querySelector('#followers-count').textContent = data.followers_count;
    })
    .catch(error => console.error('Error:', error));
}

// Helper to get CSRF token from cookies (needed for POST/PUT requests in Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
            }
        });
    }
    return cookieValue;
}