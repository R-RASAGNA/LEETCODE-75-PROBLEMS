class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            if n == 0:  # If all flowers are planted, return True early
                return True

            if flowerbed[i] == 0:  # Check if current spot is empty
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:  # Valid spot found
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1  # Reduce required flower count
                    
        return n == 0  # If all flowers were planted, return True
