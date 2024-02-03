from unittest import TestCase
import json
from pathlib import Path
from ensta.containers import CarouselUpload


SUCCESS = Path('./').joinpath('test_ensta/samples/carousel/success.json')


class PostUploadTest(TestCase):

    def test_parse_success(self):
        with open(SUCCESS) as success:
            success_data = json.load(success)
        carousel_upload = CarouselUpload.from_response_data(success_data)
        self.assertIsInstance(carousel_upload, CarouselUpload)
        self.assertEqual(carousel_upload.pk, '3294087557893039961')
        self.assertEqual(carousel_upload.carousel_media_count, len(carousel_upload.carousel_media))
