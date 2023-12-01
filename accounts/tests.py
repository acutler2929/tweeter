#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tweets.models import Tweet


class SignupPageTests(TestCase):
    """Signup Page Tests"""

    def test_url_exists_at_correct_location_signupview(self):
        """Test url exists a correct location signup view"""

        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        """Test signup view"""

        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """Test signup form"""

        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        first_user = get_user_model().objects.first()
        self.assertEqual(first_user.username, "testuser")
        self.assertEqual(first_user.email, "testuser@email.com")


class ProfileTests(TestCase):
    """Test profile functionality"""

    @classmethod
    def setUpTestData(cls):
        """Set up test data to use"""
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="testpass"
        )

        cls.tweet = Tweet.objects.create(
            body="my test tweet",
            author=cls.user,
        )

    def setUp(self):
        """log in for testing"""
        self.client.login(username="testuser", password="testpass")

    def test_url_exists_as_correct_location_profile_private(self):
        """Test url exists at correct location Profile Private"""
        response = self.client.get(f"/accounts/profile/{self.user.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_profile_public(self):
        """Test url exists at correct location Profile Public"""
        response = self.client.get(f"/accounts/public_profile/{self.tweet.author.pk}/")
        self.assertEqual(response.status_code, 200)
