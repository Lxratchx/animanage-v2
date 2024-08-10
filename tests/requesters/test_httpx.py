from unittest import TestCase
from unittest.mock import patch, MagicMock, AsyncMock
import asyncio

from requester.concretes.httpx import HttpX


class TestHttpX(TestCase):
    @patch('requester.concretes.httpx.httpx.get')
    def setUp(self, httpx_get) -> None:
        self.response_mock = MagicMock()
        self.response_mock.text = 'text page content'
        self.response_mock.content = b'bytes page content'

    @patch('requester.concretes.httpx.httpx.get')
    def test_fetch_with_sigle_url(self, httpx_get):
        """test if fetch return the valid result with the correct type when sent a sigle url
        given valid arguments
        """
        httpx_get.return_value = self.response_mock

        url = 'https://pudim.com.br'
        cases = [
            (url, 'text', False, 'text page content', str),
            (url, 'bytes', False, b'bytes page content', bytes),
        ]
        for url, content_type, use_async, expected_value, expected_instance_cls in cases:
            with self.subTest(
                url=url, content_type=content_type, 
                use_async=use_async, expected_value=expected_value,
                expected_instance_cls=expected_instance_cls
            ):
                httpx = HttpX(url, content_type, use_async)
                result = httpx.fetch()

                self.assertListEqual(
                    [result, type(result)],
                    [expected_value, expected_instance_cls]
                )

    @patch('requester.concretes.httpx.httpx.get')
    def test_fetch_with_multiple_urls(self, httpx_get):
        """test if fetch return a list of page content with the correct
        value and type given valid arguments
        """
        httpx_get.return_value = self.response_mock

        url = ['https://pudim.com.br', 'https://google.com/']
        cases = [
            (url, 'text', False, ['text page content', 'text page content'], list),
            (url, 'bytes', False, [b'bytes page content', b'bytes page content'], list),
        ]
        for url, content_type, use_async, expected_value, expected_instance_cls in cases:
            with self.subTest(
                url=url, content_type=content_type, 
                use_async=use_async, expected_value=expected_value,
                expected_instance_cls=expected_instance_cls
            ):
                httpx = HttpX(url, content_type, use_async)
                result = httpx.fetch()

                self.assertListEqual(
                    [result, type(result)],
                    [expected_value, expected_instance_cls]
                )

    @patch('requester.concretes.httpx.httpx.AsyncClient.get')
    @patch('requester.concretes.httpx.httpx.get')
    def test_fetch_using_async(self, httpx_get, async_client_get):
        """test if return the correct value when using async request"""
        httpx_get.return_value = self.response_mock
        async_client_get.return_value = self.response_mock

        httpx = HttpX('https://pudim.com.br', content_type='text', use_async=True)
        page_content = asyncio.run(httpx.fetch())
        self.assertEqual(page_content, 'text page content')

    @patch('requester.concretes.httpx.httpx.AsyncClient.get')
    @patch('requester.concretes.httpx.httpx.get')
    def test_fetch_using_async_to_multiple_urls(self, httpx_get, async_client_get):
        """test if return the correct value when using async request to multiple urls"""
        httpx_get.return_value = self.response_mock
        async_client_get.return_value = self.response_mock

        httpx = HttpX(
            [
                'https://pudim.com.br',
                'https://google.com/',
            ], 
            content_type='text',
            use_async=True
        )
        page_content = asyncio.run(httpx.fetch())
        self.assertEqual(page_content, ['text page content', 'text page content'])
