from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ="profile/")
    bio = models.TextField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, value):
        profile = cls.objects.filter(id = value).update()
        return profile

