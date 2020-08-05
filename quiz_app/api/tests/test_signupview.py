import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from quiz_app.api.models import User
from quiz_app.api.serializers import SignupSerializer


class SignupTestCase(APITestCase):
    def test_signup(self):
        data = {"email":"test@localhost.app","username":"testcase","first_name":"test","last_name":"case","password":"some_strong_psw"}
        response = self.client.post("/auth/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)