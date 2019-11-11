from django.test import TestCase
from .models import *
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name = 'harikrishna', email = 'harikrishnayadav70@gmail.com',password = 'hari123')


    def test_user_name(self):
        user = User.objects.get(name='harikrishna')
        user = User.objects.get(password = 'hari123')
        self.assertEqual(user.name,'harikrishna')
        self.assertEqual(user.password, 'hari123')


class TweetTestCase(TestCase):
    def setUp(self):
        usert =  User.objects.create(name = 'harikrishna', email = 'harikrishnayadav70@gmail.com',password = 'hari123')
        Tweet.objects.create(tweet = 'just',date = 'Nov. 9, 2019, 5:22 a.m.',user = usert )

    def test_twitter_name(self):
        room = Tweet.objects.get(tweet = 'just')
        self.assertEqual(room.tweet,'just')