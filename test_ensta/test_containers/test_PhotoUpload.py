from unittest import TestCase
import json
from pathlib import Path
from ensta.containers import PhotoUpload


SUCCESS = Path('./').joinpath('test_ensta/samples/post/success.json')


class PhotoUploadTest(TestCase):

    def test_parse_success(self):
        with open(SUCCESS) as success:
            success_data = json.load(success)
        post_upload = PhotoUpload.from_response_data(success_data)
        self.assertIsInstance(post_upload, PhotoUpload)
        self.assertEqual(post_upload.pk, '3289076043880437691')
