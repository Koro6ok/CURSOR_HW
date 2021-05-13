import unittest
from employee import Employee
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee('Volodia', 'Klychko', 1000)

    def test_email(self):
        self.assertEqual(self.classTest.email, 'Volodia.Klychko@email.com')

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, 'Volodia Klychko')

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 1050)

    @patch('requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        response = self.classTest.monthly_schedule('May')
        self.assertIsNotNone(response)

        mock_get.return_value.ok = False
        response = self.classTest.monthly_schedule('May')
        self.assertIsNotNone(response)
        self.assertEqual(response, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()
