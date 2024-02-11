from unittest import TestCase
import json
from pathlib import Path
from ensta.containers.PostDetail import Comment
from ensta.containers import PostDetail


POST_DATA = Path('./').joinpath('test_ensta/samples/post/get.json')


class PostDetailTest(TestCase):

    def test_parse_success(self):
        with open(POST_DATA) as get:
            post_data = json.load(get)
        post_detail = PostDetail.from_data(post_data)
        self.assertIsInstance(post_detail, PostDetail)
        self.assertEqual(post_detail.pk, '3289102505917171189')
        comments = post_detail.comments
        self.assertEqual(len(comments), post_detail.comment_count)
        for comment in comments:
            self.assertIsInstance(comment, Comment)
