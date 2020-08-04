from django.test import TestCase
from quiz_app.api.models import User, Profile
# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id=1, username='jorim', email='jorim.webdev@gmail.com', first_name='Jorim', last_name='Midumbi', password='moringa81')
        self.user2 = User.objects.create(id=2, username='doctar', email='doctar@gmail.com', first_name='Doc', last_name='Tar', password='doc420')
        self.user3 = User.objects.create(id=3, username='joekadenge', email='joekadenge@gmail.com', first_name='Joe', last_name='Kadenge', password='jdeng32')
    
    def test_save_profile(self):
        self.assertIsInstance(self.user1.profile, Profile)
        self.assertIsInstance(self.user2.profile, Profile)
        self.assertIsInstance(self.user3.profile, Profile)
