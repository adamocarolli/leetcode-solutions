"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {n: n}
        
        while n != 1:
            s, n = str(n), 0
            for c in s:
                n += pow(int(c), 2)
            
            if n in d:
                return False
            d[n] = n
        
        return True