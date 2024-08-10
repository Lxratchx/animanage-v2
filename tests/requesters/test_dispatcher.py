from unittest import TestCase
from requester.dispatcher import RequestDispatcher


class TestRequestDispatcher(TestCase):
    def setUp(self):
        self.dispatcher = RequestDispatcher()

        self.key = 'key'
        def f(): return 1

        self.dispatcher.add_handler(self.key, f=f)
    
    def test_dispatcher_add_handler(self):
        """test if add_handler add correctly the values to the handlers"""
        self.dispatcher._handlers = {}
        key = 'key1'
        def f2(): return 1
        self.dispatcher.add_handler(key, f=f2)
        
        self.assertDictEqual(
            self.dispatcher._handlers,
            {key: f2}
        )

    def test_dispatcher_returns_valid_func_execution(self):
        """test if the valid func return is getted given a valid key"""
        result = self.dispatcher.dispatch(self.key)
        expected = 1

        self.assertEqual(result, expected)
    
    def test_dispatcher_returns_None_if_key_does_not_exists(self):
        """test if the dispatch method return None if the given key does not exists"""
        result = self.dispatcher.dispatch('unexisting key')
        self.assertIsNone(result)
    
