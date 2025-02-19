class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # Smallest number so far
            elif num <= second:
                second = num  # Second smallest number so far
            else:
                return True  # Found a third number greater than second
        
        return False
