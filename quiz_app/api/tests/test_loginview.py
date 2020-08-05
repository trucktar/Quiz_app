# from django.test import TestCase
# from quiz_app.api.models import User
# from quiz_app.api.views import LoginAPIView, SignupAPIView

# # Create your tests here.

# class LoginAPIViewTest(TestCase):

#     def setUp(self):
#         self.user1 = User.objects.create(id=1, email='jorim.webdev@gmail.com', password='moringa81')

#     def tearDown(self):
#         self.user1.delete()

#     def test_correct(self):
#         response = self.client.post('/login/', {'email': 'jorim.webdev@gmail.com', 'password': 'moringa81'})
#         self.assertTrue(response.data['authenticated'])

#     def test_wrong_email(self):
#         response = self.client.post('/login/', {'email': 'wrong@example.com', 'password': 'moringa81'})
#         self.assertFalse(response.data['authenticated'])

#     def test_wrong_password(self):
#         response = self.client.post('/login/', {'email': 'jorim.webdev@gmail.com', 'password': 'wrong'})
#         self.assertFalse(response.data['authenticated'])
