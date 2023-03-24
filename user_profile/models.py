from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Child(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default.jpg',
        upload_to='profile_avatars'
    )
    bio = models.TextField()
    age = models.PositiveIntegerField(null=True, blank=True)
    children = models.ManyToManyField(Child, blank=True)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(max_length=8)
    child = models.ManyToManyField(Child)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
