'''
Sqrt(x)
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''

class Solution:
	def sqrt(self, x: int) -> int:
		left, right, res = 1, x, 0
		while left <= right:
			mid = (left + right) // 2
			if mid <= x / mid:
				left = mid + 1
				res = mid
			else:
				right = mid - 1
		return res