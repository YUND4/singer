"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255,default='N/A')
    description = models.CharField(max_length=255,default='N/A')

    CATEGORIES = (
        ('I', 'INFRASTRUCTURA'),
        ('E', 'EDUCACION'),
        ('S', 'SALUD'),
        ('T', 'TRANSPORTE'),
        ('B', 'BIENESTAR CIUDADANO'),
        ('O', 'OTRA'),
    )
    categories = models.CharField(max_length=20)

    city = models.CharField(max_length=255,default='N/A')
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
