from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Manager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'
    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name='نویسنده')
    # data fields
    title = models.CharField(max_length=250, verbose_name='موضوع')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=250, verbose_name='اسلاگ')
    # date fields
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # choice fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title


class Ticket(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=250)




















