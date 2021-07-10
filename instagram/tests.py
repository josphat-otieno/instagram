from django.test import TestCase
from .models import Profile
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
        