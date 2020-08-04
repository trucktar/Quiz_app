from django.test import TestCase
from quiz_app.api.models import User
# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user = User(username='jorim', email='jorim.webdev@gmail.com', first_name='Jorim', last_name='Midumbi', password='moringa81')
        self.user.save()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()