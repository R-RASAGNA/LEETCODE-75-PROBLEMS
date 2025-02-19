class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])  # Split words, reverse list, and join with a single space
