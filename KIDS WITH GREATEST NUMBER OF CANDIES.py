class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)  # Find the maximum candies any kid currently has
        return [(candy + extraCandies) >= max_candies for candy in candies]
