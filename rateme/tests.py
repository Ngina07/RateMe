from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile, Review

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(id=1,title='new post',image='images/lagoon.jpeg',description='the best of the best', url='https://link.com/',user_id =3)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))
        
    def tearDown(self):
        Project.objects.all().delete() 


class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(profile_pic='images/lagoon.jpeg',bio='I love bikes', contacts='3455',user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def tearDown(self):
        Profile.objects.all().delete() 

class ReviewTestClass(TestCase):
    def setUp(self):
        self.review = Review(design=6,usability=5,content=4,average='5',user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.review,Review))

    def tearDown(self):
        Review.objects.all().delete()