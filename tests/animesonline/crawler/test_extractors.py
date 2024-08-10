from unittest import TestCase
from unittest.mock import Mock
from animesonline.crawler.extractors import AnimeExtractor, AbstractRequester


class TestAnimeExtractor(TestCase):
    def setUp(self) -> None:
        absmock = Mock(spec=AbstractRequester)
        absmock.fetch.return_value = 'page with many data of anime'
        self.fake_requester = Mock()
        self.fake_requester.return_value = absmock
    
    def test_extract_method_return_an_list_with_unique_page_content_when_npges_eq_1(self):
        """verify if the extract method return the page content correctly
        with just one page
        """
        extractor = AnimeExtractor(self.fake_requester, npages=1)
        result = extractor.extract()
        expected = ['page with many data of anime']
        self.assertListEqual(result, expected)
    
    def test_extract_method_return_an_list_with_all_page_content(self):
        """verify if the extract method return the page content correctly
        when npages > 1
        """
        extractor = AnimeExtractor(self.fake_requester, npages=3)
        result = extractor.extract()
        expected = ['page with many data of anime'] * 3
        self.assertListEqual(result, expected)
