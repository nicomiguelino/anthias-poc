from unittest import TestCase
from unittest.mock import patch, Mock

from src.blog import Blog


class TestBlog(TestCase):
    @patch('src.blog.Blog')
    def test_blog_posts(self, MockBlog):
        mock_blog = MockBlog()
        mock_blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'A long time ago, in a galaxy far, far away...'
            },
        ]

        response = mock_blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions

        assert MockBlog.called

        mock_blog.posts.assert_called_with()
        mock_blog.posts.assert_called_once_with()

        # The assertion below will fail.
        # mock_blog.posts.assert_called_once_with(1, 2, 3)

        mock_blog.reset_mock()
        mock_blog.posts.assert_not_called()
