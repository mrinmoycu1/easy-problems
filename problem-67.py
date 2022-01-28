'''
Add Binary
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        
        sum = a1 + b1
        return bin(sum)[2:]
