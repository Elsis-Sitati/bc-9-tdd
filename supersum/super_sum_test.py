import unittest
from super_sum import super_sum

class TestSuperSum(unittest.TestCase):

	def test_firs_test(self):
		''' The sum of elements in one list should return 30'''
		self.assertEqual(super_sum(10,5,6,9), 30)

	def test_two(self):
		''' The sum of elements in a given list and number should return the sum of lists and number '''
		self.assertEqual(super_sum([6,78], 2, 1), 87)

	def test_three(self):
		'''testing if nothing is passed'''
		self.assertNotEqual(super_sum(''), None , msg= 'should return /None')

	def test_four(self):
		''' the sum of elements of all elements from all lists '''
		self.assertEqual(super_sum([10,3], [2,5], [8,1]), 29)

	def test_five(self):
		'''throwing exceptions if  a string  is passed'''
		result = super_sum()
		self.assertNotEqual(type(result), int , msg= 'Put an integer')

	def test_six(self):
		''' The sum of elements in lists and numbers should return the total sum of elements in lists and numbers '''
		self.assertEqual(super_sum([1,1], [1,1], 1), 5)


	
if __name__ == '__main__':
	unittest.main()

