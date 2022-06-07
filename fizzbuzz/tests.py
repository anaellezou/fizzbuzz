import unittest
import json
import gzip
import fizzbuzz

# Tests GET fizzbuzz endpoint
class FizzBuzzTests(unittest.TestCase):

    def setUp(self):
        self.app = fizzbuzz.app.test_client()

    def test_get_homepage(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_fizzbuzz(self):
        rv = self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        data = gzip.decompress(rv.data)
        fizzbuzz = json.loads(data.decode())
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(len(fizzbuzz), 15)
        self.assertEqual(fizzbuzz, [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz'])
    
    def test_fizzbuzz_missing_parameter(self):
        rv = self.app.get('/fizzbuzz?int1=1&int2=100&limit=100&str1=fizz')
        fizzbuzz = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz, "Error: arguments cannot be None")
    
    def test_fizzbuzz_int_zero(self):
        rv = self.app.get('/fizzbuzz?int1=0&int2=5&limit=100&str1=fizz&str2=buzz')
        fizzbuzz = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz, "Error: given number must be greater than 0")

    def test_fizzbuzz_negative_int(self):
        rv = self.app.get('/fizzbuzz?int1=-5&int2=5&limit=100&str1=fizz&str2=buzz')
        fizzbuzz = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz, "Error: given number must be greater than 0")

    def test_fizzbuzz_invalid_parameter_value(self):
        rv = self.app.get('/fizzbuzz?int1=1&int2=100&limit=50&str1=fizz&str2=test')
        fizzbuzz = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(fizzbuzz, "Error: wrong strings were given")
