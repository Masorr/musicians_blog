from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    '''
    Stores a single blog post entry related to :model:`auth.User`
    '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    '''
    Stores comments related to a :model:`Post` made by :model:`auth.User`
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


# Create user profile model
class Profile(models.Model):
    '''
    Stores user profile information related to :model:`auth.User`.

    One user is associated with one profile
    Follows symmetrical = false, stating if you follow someone,
    they don't have to follow you
    blank=True, you don't need to have followers or be followed
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="followed_by"
    )
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Makes a profile upon newly made user
@receiver(post_save, sender=User)
def make_profile(sender, instance, created, **kwargs):
    '''
    Creates a profile for a newly created user and sets initial
    follow relationships.
    '''
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
