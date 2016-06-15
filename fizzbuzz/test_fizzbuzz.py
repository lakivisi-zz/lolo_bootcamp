import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	'''Testing the fizzbuzz
	'''
	def test_returns_fizz_when_divisible_by_three(self):
		'''
		Test that returns fizz when input is divisible by three
		'''
		self.assertEqual(fizzbuzz.fizz(3),'Fizz')

	def test_returns_buzz_when_divisible_by_five(self):
		'''
		Test that returns fizz when input is divisible by five
		'''
		self.assertEqual(fizzbuzz.fizz(5),'Buzz')

	def test_returns_fizzbuzz_when_divisible_by_both_three_and_five(self):
		'''
		Test that returns fizz when input is divisible by three and five
		'''
		self.assertEqual(fizzbuzz.fizz(15),'FizzBuzz')

	def test_returns_not_divisible_when_not_divisible_by_both_three_and_five(self):
		'''
		Test that returns fizz when input is not divisible by three and five
		'''
		self.assertEqual(fizzbuzz.fizz(17),'Number not divisible by 3 and 5')

	




