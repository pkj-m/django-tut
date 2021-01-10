from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # this method is run whenever we save a Profile object
    def save(self, **kwargs):
        # run the super class' save method 
        super().save()

        # open the image using Pillow library
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_sz = (300, 300)
            img.thumbnail(output_sz)
            img.save(self.image.path)



