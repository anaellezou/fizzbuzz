""" Fizzbuzz API test file """
import unittest
import json
import gzip
import fizzbuzz

# Tests GET fizzbuzz endpoint
class FizzBuzzTests(unittest.TestCase):
    """ Tests fizzbuzz API endpoints """

    def setUp(self):
        self.app = fizzbuzz.app.test_client()

    # pylint: disable=invalid-name
    def test_get_homepage(self):
        """ Test GET Homepage """
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    # pylint: disable=invalid-name
    def test_fizzbuzz(self):
        """ Test fizzbuzz endpoint with a simple valid query """
        rv = self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        data = gzip.decompress(rv.data)
        fizzbuzz_data = json.loads(data.decode())
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(len(fizzbuzz_data), 15)
        self.assertEqual(
            fizzbuzz_data,
            [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
        )

    # pylint: disable=invalid-name
    def test_fizzbuzz_missing_parameter(self):
        """ Test fizzbuzz endpoint with a missing parameter """
        rv = self.app.get('/fizzbuzz?int1=1&int2=100&limit=100&str1=fizz')
        fizzbuzz_data = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz_data, "Error: arguments cannot be None")

    # pylint: disable=invalid-name
    def test_fizzbuzz_int_zero(self):
        """ Test fizzbuzz endpoint passing a zero as argument """
        rv = self.app.get('/fizzbuzz?int1=0&int2=5&limit=100&str1=fizz&str2=buzz')
        fizzbuzz_data = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz_data, "Error: given number must be greater than 0")

    # pylint: disable=invalid-name
    def test_fizzbuzz_negative_int(self):
        """ Test fizzbuzz endpoint with a negative int """
        rv = self.app.get('/fizzbuzz?int1=-5&int2=5&limit=100&str1=fizz&str2=buzz')
        fizzbuzz_data = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz_data, "Error: given number must be greater than 0")

    # pylint: disable=invalid-name
    def test_fizzbuzz_invalid_parameter_value(self):
        """ Test fizzbuzz endpoint with an invalid parameter value """
        rv = self.app.get('/fizzbuzz?int1=1&int2=100&limit=50&str1=fizz&str2=test')
        fizzbuzz_data = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz_data, "Error: wrong strings were given")
