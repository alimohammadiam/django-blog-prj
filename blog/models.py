from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


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
    reading_time = models.PositiveIntegerField(default=0, verbose_name='زمان مطالعه')

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

    def get_absolute_url(self):
        return reverse('blog:posts_detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for img in self.images.all():
            storage, path = img.image_file.storage, img.image_file.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class Ticket(models.Model):
    message = models.TextField(verbose_name='پیام')
    name = models.CharField(max_length=250, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    subject = models.CharField(max_length=250, verbose_name='موضوع')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='پست')
    name = models.CharField(max_length=250, verbose_name='نام')
    body = models.TextField(verbose_name='متن کامنت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آپدیت')
    active = models.BooleanField(default=False, verbose_name='وضعیت')

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'{self.name}: {self.post}'


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', verbose_name='تصویر')
    image_file = ResizedImageField(upload_to="post_images/", size=[500, 500], quality=75, crop=['middle', 'center'])
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    created = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image_file.storage, self.image_file.path
        storage.delete(path)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها '


#    # یه باگ داره که وقتب برای تصاویر title ننویسیم ارور میده
    # def __str__(self):
    #     if self.title:
    #         return self.title













