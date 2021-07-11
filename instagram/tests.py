from django.test import TestCase
from .models import Profile, Images
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.bio =Profile(bio = "i love instagram")

    def test_instance(self):
        self.assertTrue(isinstance(self.bio, Profile))

    def test_save_method(self):
        self.bio.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_dalete_profile(self):
        self.bio.save_profile()
        profile = Profile.objects.all()
        self.bio.delete_profile()
        self.assertTrue(len(profile)==0)

    def test_update_profile(self):
        self.bio.save_profile()
        profile = Profile.objects.filter(self.bio)
        self.bio.update_profile()
        self.bio.save_profile()
        self.assertTrue(len(profile)==1)

class TestImage(TestCase):
    def setUp(self):
        self.bio = Profile(bio = 'i love instagram')
        self.bio.save_profile()

        self.new_image = Images(image_name='jose', image_caption = 'you look good', profile=self.bio)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Images))
        

    def tearDown(self):
        Profile.objects.all().delete()
        Images.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)

    def test_update_caption(self):
        self.new_image.save_image()
        image = Images.objects.filter(self.new_image)
        self.new_image.update_caption()
        self.new_image.save_image()
        self.assertTrue(len(image)==1)

    

    

    

    
        


        