#   Alice Cutler
#   CIS 218
#   November 24, 2023
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet, Reply


class TweetTests(TestCase):
    """Tweet Tests"""

    # SETTING UP DATA ---------------------------------------------------
    @classmethod
    def setUpTestData(cls):
        """Set up test data to use"""
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="testpass"
        )

        # TODO: MAYBE CREATE A SECOND USER THAT IS NOT LOGGED IN
        # TO TEST PUBLIC PROFILE VIEW ???
        cls.tweet = Tweet.objects.create(
            body="my test tweet",
            author=cls.user,
        )

        cls.reply = Reply.objects.create(
            tweet=cls.tweet,
            reply="my test reply",
            author=cls.user,
        )

    # TESTING MODELS ----------------------------------------------------
    def test_tweet_model(self):
        """Test the tweet model"""

        self.assertEqual(self.tweet.body, "my test tweet")
        self.assertEqual(self.tweet.author.username, "testuser")
        self.assertEqual(self.tweet.get_absolute_url(), "/tweets/1/")

    def test_reply_model(self):
        """Test the reply model"""

        self.assertEqual(self.reply.tweet.body, "my test tweet")
        self.assertEqual(self.reply.reply, "my test reply")
        self.assertEqual(self.reply.author.username, "testuser")

    # TESTING URLS ------------------------------------------------------
    def test_url_exists_as_correct_location_feed(self):
        """Test url exists at correct location Feed"""
        # TODO: SEE IF THERE IS A WAY TO DO THIS ONLY ONCE...
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/tweets/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_detail(self):
        """Test url exists at correct location Detail"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/tweets/{self.tweet.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_new_tweet(self):
        """Test url exists at correct location New Tweet"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/tweets/new/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_edit_tweet(self):
        """Test url exists at correct location Edit Tweet"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/tweets/{self.tweet.pk}/edit/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_delete_tweet(self):
        """Test url exists at correct location Delete Tweet"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(f"/tweets/{self.tweet.pk}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_as_correct_location_profile_private(self):
        """Test url exists at correct location Profile Private"""
        self.client.login(username="testuser", password="testpass")
        # TODO
        pass

    def test_url_exists_as_correct_location_profile_public(self):
        """Test url exists at correct location Profile Public"""
        self.client.login(username="testuser", password="testpass")
        # TODO
        pass

    # TESTING VIEWS -----------------------------------------------------
    def test_tweet_feed_view(self):
        """Test Tweet Feed View"""

        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("tweet_feed"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my test tweet")
        self.assertTemplateUsed(response, "tweet_feed.html")

    def test_tweet_detail_view(self):
        """Test Tweet Detail View"""

        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("tweet_detail", kwargs={"pk": self.tweet.pk})
        )
        no_response = self.client.get("/tweets/-1/")

        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
        self.assertTemplateUsed(response, "tweet_detail.html")

    def test_profile_private_view(self):
        """Test Profile Private View"""
        pass

    # TODO: MAYBE CREATE A SECOND USER THAT IS NOT LOGGED IN
    # TO TEST PUBLIC PROFILE VIEW ???
    def test_profile_public_view(self):
        """Test Profile Public View"""
        pass

    # TESTING CREATE-UPDATE-DELETE --------------------------------------
    def test_new_tweet(self):
        """Test New Tweet"""

        # TODO: FOR SOME REASON, THIS DOESN'T POST A NEW TWEET OBJECT
        response = self.client.post(
            reverse("tweet_new"),
            {
                "body": "another test tweet",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tweet.objects.last().body, "another test tweet")
        self.assertEqual(Tweet.objects.last().author.pk, self.user.id)

    def test_edit_tweet(self):
        """Test Edit Tweet"""

        # TODO: FOR SOME REASON, THIS DOESN'T EDIT A TWEET OBJECT
        response = self.client.post(
            reverse("tweet_edit", args=str(self.tweet.pk)),
            {
                "body": "my updated tweet",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tweet.objects.last().body, "my updated tweet")
        self.assertEqual(Tweet.objects.last().author.pk, self.user.id)

    def test_add_reply(self):
        """Test Add Reply"""

        # TODO: FOR SOME REASON, THIS DOESN'T POST A NEW REPLY OBJECT
        response = self.client.post(
            reverse("tweet_detail", args=str(self.tweet.pk)),
            {"body": "my other test reply"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reply.objects.last().tweet.body, "my updated tweet")
        self.assertEqual(Reply.objects.last().reply, "my other test reply")
        self.assertEqual(Reply.objects.last().author.pk, self.user.id)

    def test_delete_tweet(self):
        """Test Delete_Tweet"""

        response = self.client.post(reverse("tweet_delete", args=str(self.tweet.pk)))
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(Tweet.objects.last().body, "my updated tweet")
