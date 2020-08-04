from django.test import TestCase
from quiz_app.api.models import User
# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id=1, username='jorim', email='jorim.webdev@gmail.com', first_name='Jorim', last_name='Midumbi', password='moringa81')
        self.user2 = User.objects.create(id=2, username='doctar', email='doctar@gmail.com', first_name='Doc', last_name='Tar', password='doc420')
        self.user3 = User.objects.create(id=3, username='joekadenge', email='joekadenge@gmail.com', first_name='Joe', last_name='Kadenge', password='jdeng32')

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user1, User))
        self.assertTrue(isinstance(self.user2, User))
        self.assertTrue(isinstance(self.user3, User))

    def test_save_user(self):
        self.assertTrue(self.user1.username == 'jorim')
        self.assertTrue(self.user2.username == 'doctar')
        self.assertTrue(self.user3.username == 'joekadenge')

    # def test_delete_user(self):
    #     self.user1.delete()
    #     self.user2.delete()
    #     self.user3.delete()