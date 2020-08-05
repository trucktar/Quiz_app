import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from quiz_app.api.models import User
from quiz_app.api.serializers import ProfileSerializer


class ProfileTestCase(APITestCase):

    profile_url = reverse("profile")

    def setup(self):
        self.user = User.objects.create_user(email="test@localhost.app", username="testcase", first_name="test", last_name="case")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_fields_authenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_profile_fields_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  


