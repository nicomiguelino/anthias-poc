from unittest import TestCase
from unittest.mock import patch
from src.calculator import Calculator


def mock_sum(a, b):
    """
    A mock sum function without the long running time.sleep.
    """

    return a + b


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_1(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    @patch('src.calculator.Calculator.sum', return_value=9)
    def test_sum_2(self, mock_sum):
        self.assertEqual(mock_sum(2, 3), 9)

    @patch('src.calculator.time.sleep', side_effect=(lambda _: None))
    def test_sum_3(self, mock_sleep):
        self.assertEqual(self.calc.sum(4, 3, sleep=True), 7)
        mock_sleep.assert_called_once()

    @patch('src.calculator.Calculator.sum', side_effect=mock_sum)
    def test_sum_4(self, sum):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(7, 3), 10)
