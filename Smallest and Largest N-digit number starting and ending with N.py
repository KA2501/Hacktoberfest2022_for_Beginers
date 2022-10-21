# Python3 program for the
# above approach
import math

# Function to find n digit
# largest number starting
#and ending with n
def findNumberL(n):

	# Corner Case when n = 1
	if (n == 1):
		return "1"

	# Result will store the
	# n - 2*length(n) digit
	# largest number
	result = ""

	# Find the number of
	# digits in number n
	length = math.floor(math.log10(n) + 1)

	# Append 9
	for i in range(1, n - (2 *
				length) + 1):
		result += '9'
		
	# To make it largest n digit
	# number starting and ending
	# with n, we just need to
	# append n at start and end
	result = (str(n) + result +
			str(n))

	# Return the largest number
	return result

# Function to find n digit
# smallest number starting
# and ending with n
def findNumberS(n):

	# Corner Case when n = 1
	if (n == 1):
			return "1"

	# Result will store the
	# n - 2*length(n) digit
	# smallest number
	result = ""

	# Find the number of
	# digits in number n
	length = math.floor(math.log10(n) + 1)
	
	for i in range(1, n -
				(2 * length) + 1):
		result += '0'

	# To make it smallest n digit
	# number starting and ending
	# with n, we just need to
	# append n at start and end
	result = (str(n) + result +
			str(n))

	# Return the smallest number
	return result

# Driver Code
if __name__ == "__main__":

	# Given Number
	N = 3

	# Function Call
	print("Smallest Number = " + findNumberS(N))
	print("Largest Number = "+ findNumberL(N))
