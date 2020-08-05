from django.test import TestCase
from django.urls import reverse
from quiz_app.api.models import User
from quiz_app.api.views import LoginAPIView, SignupAPIView
from authentication.utils import generate_token
# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.signup_url=reverse('signup')
        self.login_url=reverse('login')
        self.user={
            'email':'testemail@gmail.com',
            'username':'username',
            'first_name':'first',
            'last_name':'last',
            'password':'password'
        }
       
        self.user_unmatching_password={

            'email':'testemail@gmail.com',
            'username':'username',
            'first_name':'first',
            'last_name':'last',
            'password':'pssword'
        }

        self.user_invalid_email={
            
            'email':'test.com',
            'username':'username',
            'first_name':'first',
            'last_name':'last',
            'password':'password'
        }
        return super().setUp()