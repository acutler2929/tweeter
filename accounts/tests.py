#       Alice Cutler
#       CIS 218
#       October 25, 2023
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


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
