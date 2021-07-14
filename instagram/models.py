from collections import UserDict
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, value):
        profile = cls.objects.filter(id = value).update()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

# def create_profile(sender, **kwargs):
#         if kwargs['created']:
#             user_profile = Profile.objects.create(user = kwargs['instance'])
# post_save.connect(create_profile, sender=User)


class Images(models.Model):
    image = ImageField(upload_to = "images/")
    image_name = CharField(max_length=30) 
    image_caption = TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        

    def total_likes(self):
        return self.like.count()  
        #vote_count = Item.objects.filter(votes__contest=contestA).count()

    @classmethod
    def update_caption(cls, id, value):
        image = cls.objects.filter(id=id).update(image_caption=value)
        return image

   

class Comment(models.Model):
    name = models.CharField(max_length=60, default='')
    comments = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    images = models.ForeignKey(Images, related_name = 'comments',on_delete=CASCADE)

    def __str__(self):
        return '%s - %s' %(self.images.image_name, self.name)

    def save_comment(self):
        self.save()

    def delete_commnet(self):
        self.delete()

        



    

