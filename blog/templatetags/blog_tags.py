from django import template
from ..models import Post, Comment, User
from django.db.models import Count, Max, Min, Sum
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


# simple tags
@register.simple_tag()
def total_posts():
    return Post.published.count()


@register.simple_tag()
def total_comment():
    return Comment.objects.filter(active=True).count()


@register.simple_tag()
def last_post_date():
    return Post.published.last().publish


@register.simple_tag()
def most_popular_posts(count=4):
    return Post.published.annotate(comment_count=Count('comments')).order_by('-comment_count')[:count]


@register.simple_tag()
def max_reading_time():
    return Post.published.annotate(max_time=Max('reading_time')).order_by('-max_time')[:1]


@register.simple_tag()
def min_reding_time():
    return Post.published.annotate(min_time=Min('reading_time')).order_by('min_time')[:1]
    # return Post.published.aggregate(Min('reading_time'))


@register.simple_tag()
def most_popular_user(count=3):
    return User.objects.annotate(max_posts=Count('user_posts')).order_by('-max_posts')[:count]


# inclusion tags
@register.inclusion_tag("partials/latest_post.html")
def latest_posts(count=4):
    l_posts = Post.published.order_by('-publish')[:count]
    context = {
        'l_posts': l_posts
    }
    return context


@register.filter(name='markdown')
def to_markdown(text):
    return mark_safe(markdown(text))




