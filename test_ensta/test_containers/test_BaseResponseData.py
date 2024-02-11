from typing import List
from unittest import TestCase
from dataclasses import dataclass
from ensta.containers.BaseResponseData import BaseResponseData


class BaseResponseDataTest(TestCase):

    def test_parse_simple_data(self):
        @dataclass
        class SimpleDataclass(BaseResponseData):
            a: int
            b: float
            c: str

        expected = SimpleDataclass(a=1, b=1., c='1')

        result = SimpleDataclass.from_data({
            'a': 1,
            'b': 1.,
            'c': '1'
        })

        self.assertEqual(result, expected)

    def test_parse_with_dataclass(self):
        @dataclass
        class SimpleDataclass:
            a: int
            b: float
            c: str

        @dataclass
        class WithDataclass(BaseResponseData):
            dataclass: SimpleDataclass

        expected = WithDataclass(dataclass=SimpleDataclass(a=1, b=1., c='1'))

        result = WithDataclass.from_data({'dataclass': {
            'a': 1,
            'b': 1.,
            'c': '1'
        }})

        self.assertEqual(result, expected)

    def test_parse_with_response_data(self):
        @dataclass
        class SimpleDataclass(BaseResponseData):
            a: int
            b: float
            c: str

        @dataclass
        class WithDataclass(BaseResponseData):
            dataclass: SimpleDataclass

        expected = WithDataclass(dataclass=SimpleDataclass(a=1, b=1., c='1'))

        result = WithDataclass.from_data({'dataclass': {
            'a': 1,
            'b': 1.,
            'c': '1'
        }})

        self.assertEqual(result, expected)

    def test_parse_with_list_any(self):

        @dataclass
        class WithList(BaseResponseData):

            top_likers: List

        expected = WithList(top_likers=[1, 1., '1'])
        result = WithList.from_data({
            'top_likers': [1, 1., '1']
        })

        self.assertEqual(result, expected)

    def test_parse_with_list_str(self):

        @dataclass
        class WithList(BaseResponseData):

            top_likers: List[str]

        expected = WithList(top_likers=['a', 'b', 'c'])
        result = WithList.from_data({
            'top_likers': ['a', 'b', 'c']
        })

        self.assertEqual(result, expected)

    def test_parse_with_list_dataclass(self):

        @dataclass
        class User:
            username: str

        @dataclass
        class WithList(BaseResponseData):

            top_likers: List[User]

        expected = WithList(top_likers=[User(username='a')])
        result = WithList.from_data({
            'top_likers': [{'username': 'a'}]
        })

        self.assertEqual(result, expected)
