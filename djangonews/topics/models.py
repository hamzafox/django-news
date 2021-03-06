from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

from tinymce import HTMLField

# Create your models here.

class Topic(models.Model):
    published_at = models.DateTimeField(blank=False, null=False, default=timezone.now() )
    title = models.CharField(blank=False, null=False, max_length=100)
    slug = models.CharField(blank=False, null=False, unique=True,max_length=100)
    content = HTMLField('Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author of the Topic')
    nbr_upvotes = models.IntegerField(blank=False, null=False, default=0)
    nbr_comments = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        db_table = 'topics'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    published_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    content = models.TextField(blank=False, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments', verbose_name='related Topic')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author of the comment')

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content[:10]


class Upvote(models.Model):
    timestamp = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='upvotes', verbose_name='Upvoted Topic')
    upvoter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User who upvoted')

    class Meta:
        db_table = 'upvotes'

    def __str__(self):
        return '{} upvoted the Topic: {}'.format(self.upvoter.get_username(), self.topic.title)

    
    