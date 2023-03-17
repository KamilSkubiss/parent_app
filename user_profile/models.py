from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default.jpg',
        upload_to='profile_avatars'
    )
    bio = models.TextField()
    age = models.PositiveIntegerField(null=True, blank=True)
    number_of_children = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
