import unittest

from my_sum import my_sum

# create a class that inherits from unittests

class MySumTests(unittest.TestCase):
	def setUp(self):
		# TestCase knows to run setup first
		pass

	def test_sums_of_numbers(self):
		'''test sum of digit'''
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(my_sum(10,15),25)
		self.assertEqual(my_sum(0,0),0)
		self.assertEqual(my_sum(-8,20),12)
		self.assertEqual(my_sum(-5,-4),-9)
		self.assertEqual(my_sum (80,20),100)
		self.assertEqual(my_sum(-5,-2),-7)

	def test_non_numbers(self):
		'''
		Assert throwig of exceptions when it is
		a non number
		'''
	self.assertEqual(my_sum('d','e'),"invalid")



if __name__ == '__main__':
	unittest.main()
