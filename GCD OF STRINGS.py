
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenation in both orders isn't equal, there's no common divisor
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))

        # Return the substring of str1 with the computed GCD length
        return str1[:gcd_length]
