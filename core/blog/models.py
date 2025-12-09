from django.db import models
from treebeard.mp_tree import MP_Node

from accounts.models import User

from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse



class Category(MP_Node):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name        = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)

    def _blog_image_path(instance, filename):
        title = getattr(instance, 'title', None) or 'untitled'
        safe_title = slugify(title)
        return f'blog_images/{safe_title}/{filename}'
    
    image       = models.ImageField(upload_to=_blog_image_path, null=True, blank=True)
    content     = models.TextField()
    tag         = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    status      = models.CharField(
                                   max_length=20,
                                   choices=[('draft', 'Draft'), ('published', 'Published')],
                                   default='draft'
                                   )
    # comment     = models.ForeignKey('Comment')
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:api-v1:post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post        = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    email       = models.EmailField()
    content     = models.TextField()
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.author:
            return f"Comment by {self.author} on {self.post}"
        return f"Comment by {self.name or 'Anonymous'} on {self.post}"
    

class Like(models.Model):
    post        = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'Like by {self.user.username} on {self.post.title}'

class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('haha', 'Haha'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]

    post        = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='reactions')
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    created_at  = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'user', 'reaction_type')

    def __str__(self):
        return f'{self.reaction_type} by {self.user.username} on {self.post.title}'




