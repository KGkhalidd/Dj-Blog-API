from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'pass'
        )
        cls.post = Post.objects.create(
            author = cls.user,
            title = 'a title',
            body = 'a body'
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username , 'testuser')
        self.assertEqual(self.post.title , 'a title')
        self.assertEqual(self.post.body , 'a body')
        self.assertEqual(str(self.post) , 'a title')