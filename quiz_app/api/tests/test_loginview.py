import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from quiz_app.api.models import User
from quiz_app.api.serializers import LoginSerializer


class LoginTestCase(APITestCase):
    def test_login(self):
        data = {"email":"test@localhost.app","password":"some_strong_psw"}
        response = self.client.post("/auth/login/", data)
        self.assertTrue(response.status_code, status.HTTP_200_OK)