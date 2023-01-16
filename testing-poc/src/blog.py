import requests

POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get(POSTS_URL)
        return response.json()

    def __repr__(self):
        return f'<Blog: {self.name}>'
