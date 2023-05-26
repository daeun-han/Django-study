from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0) # 0또는 양수만 받는 필드
    lion_emoji = models.ManyToManyField(User, related_name='lion_emoji_posts', blank=True)
    lion_emoji_count = models.PositiveIntegerField(default=0) # 0또는 양수만 받는 필드
    published_date = models.DateTimeField(default=timezone.now)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    
    likes = models.ManyToManyField(User, related_name='like_comments', blank=True)
    like_count = models.PositiveIntegerField(default=0) # 0또는 양수만 받는 필드