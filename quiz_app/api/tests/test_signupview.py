import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import User
from api.serializers import SignupSerializer


class BaseTest(TestCase):
    def setUp(self):
        self.signup_url=reverse('SignupAPIView')
        self.login_url=reverse('LoginAPIView')
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


class SignupAPIViewTest(BaseTest):

   def test_can_view_page_correctly(self):
       response=self.client.get(self.signup_url)
       self.assertEqual(response.status_code,200)

   def test_can_register_user(self):
        response=self.client.post(self.signup_url,self.user,format='text')
        self.assertEqual(response.status_code,302)
   
   def test_cant_register_user_with_unmatching_passwords(self):
        response=self.client.post(self.signup_url,self.user_unmatching_password,format='text')
        self.assertEqual(response.status_code,400)

   def test_cant_register_user_with_invalid_email(self):
        response=self.client.post(self.signup_url,self.user_invalid_email,format='text')
        self.assertEqual(response.status_code,400)

   def test_cant_register_user_with_taken_email(self):
        self.client.post(self.signup_url,self.user,format='text')
        response=self.client.post(self.signup_url,self.user,format='text')
        self.assertEqual(response.status_code,400)