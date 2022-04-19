from django.test import TestCase
from .models import Post, Neighbourhood,Business,Profile
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.Cynthia = User(username = 'Cynthia',email = 'appscynthia7@gmail.com')
        self.Cynthia = Profile(user = self.Cynthia,user_id = 1,bio = 'my hood', email='test@gmail.com',profile_pic = 'image.jpg',location='Nairobi', neighbourhood='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Cynthia,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.Cynthia.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new= Neighbourhood(name ='Nairobi',location = 'Nairobi',image = 'trial.jpg',description = 'I like your my hood',user = 'Cynthia',hood_logo= 'logo.jpeg', emergency_contact= '911',occupants_count ='10')


    def test_save_image(self):
        self.image.save_image()
        image = Neighbourhood.objects.all()
        self.assertEqual(len(Neighbourhood),1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image_list = Neighbourhood.objects.all()
        self.assertTrue(len(Neighbourhood)==0)

    def test_get_all_images(self):
        self.image.save_image()
        all_images = Neighbourhood.get_all_images()
        self.assertTrue(len(Neighbourhood) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_pic = Post.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)



class BusinessTestCase(TestCase):


    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(Business),1)

    def test_delete_image(self):
        self.name.save_image()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(Business)==0)

    def test_get_all_images(self):
        self.name.save_name()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_name = Business.get_one_name(self.food.id)
        self.assertTrue(one_name.name == self.name.name)



class PostTestCase(TestCase):
    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(Post),1)

    def test_delete_image(self):
        self.name.save_name()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(Post)==0)

    def test_get_all_images(self):
        self.name.save_image()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_name = Post.get_one_name(self.food.id)
        self.assertTrue(one_name.name == self.name.name)