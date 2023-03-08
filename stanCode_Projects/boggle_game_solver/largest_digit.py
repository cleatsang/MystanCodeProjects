"""
File: largest_digit.py
Name: Audrey Tsang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	This program recursively prints the biggest digit in different integers.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: 'n' is a number of different integers.
	:return: The biggest digit we found from the helper function.
	"""
	#  Create a helper function because we need another variable to store the maximum number.
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, best):
	"""
	:param n: 'n' is a number of different integers.
	:param best: A variable used to store the maximum number.
	:return best: The variable of biggest digit.
	"""
	#  Base Case!
	if n == 0:
		return best
	else:
		#  Check if the number is negative.
		if n < 0:
			n = -n
		#  Compares the last digit with best.
		if n % 10 >= best:
			best = n % 10	 # If the new digit is bigger, refresh the best number.
		n = int(n / 10)	 # Get the rest of the numbers.
		#  Recursion
		return find_largest_digit_helper(n, best)


if __name__ == '__main__':
	main()
