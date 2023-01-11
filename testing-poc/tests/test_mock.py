import unittest
from datetime import datetime
from nose.plugins.attrib import attr
from mock import MagicMock, Mock
from requests.exceptions import Timeout
from src.my_calendar import get_holidays, is_weekday


class ProductionClass:
    def method(self):
        return 24


class MockTestCase(unittest.TestCase):
    def test_something(self):
        thing = ProductionClass()
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')

    def test_is_weekday(self):
        tuesday = datetime(year=2019, month=1, day=1)
        saturday = datetime(year=2019, month=1, day=5)

        mock_datetime = Mock()
        mock_datetime.today.return_value = tuesday
        self.assertTrue(is_weekday(mock_datetime))

        mock_datetime.today.return_value = saturday
        self.assertFalse(is_weekday(mock_datetime))

    def test_get_holidays_timeout(self):
        mock_requests = Mock()
        mock_requests.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_holidays(mock_requests)
