from unittest import TestCase
from parser.concretes.soup import SoupParser


class TestSoupParser(TestCase):
    def test_parser_select_with_an_valid_query(self):
        """test if return is valid given a valid query"""
        with open('tests/sample.html', 'r') as f:
            parser = SoupParser(f.read())
            result = parser.select('ul li')
            self.assertEqual(
                str(result),
                '[<li>value1</li>, <li>value2</li>, <li>value3</li>]'
            )
    
    def test_parser_select_with_an_invalid_query(self):
        """test if return a empty list when given a invalid query"""
        with open('tests/sample.html', 'r') as f:
            parser = SoupParser(f.read())
            result = parser.select('ol li')
            self.assertListEqual(
                result,
                []
            )
