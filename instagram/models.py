from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField

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


class Images(models.Model):
    image = ImageField(upload_to = "images/")
    image_name = CharField(max_length=30)
    image_caption = TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, value):
        image = cls.objects.filter(id=id).update(image_caption=value)
        return image

class Comment(models.Model):
    comments = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    images = models.ForeignKey(Images, on_delete=CASCADE)

    def __str__(self):
        return self.comments



    

