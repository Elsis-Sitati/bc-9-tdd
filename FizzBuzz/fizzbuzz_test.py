import unittest

from fizzbuzz import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

	def test_one(self):
		self.assertEqual(fizz_buzz(9), 'Fizz', msg="Should return 'Fizz' for multiples of 3")
	
	def test_two(self):
		self.assertEqual(fizz_buzz(50), 'Buzz', msg="Should return 'Fizz' for multiples of 5")

	def test_three(self):
		self.assertEqual(fizz_buzz(45), 'FizzBuzz', msg="Should return 'Buzz' for multiples of 3 and 5")

	def test_four(self):
		self.assertEqual(fizz_buzz(60), 'FizzBuzz', msg="Should return 'FizzBuzz' for multiples of 3 and 5")

	def test_five(self):
		self.assertEqual(fizz_buzz(53),53,  msg="Should return 'not divisible by 3 and 5'")

	def test_six(self):
		self.assertEqual(fizz_buzz(27), 'Fizz', msg="Should return 'Fizz' for multiples of 3")

if __name__ == '__main__':
	unittest.main()