"""
LeetCode Problem 605: Can Place Flowers
Difficulty: Easy

Problem:
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
1 means not empty, and an integer n, return true if n new flowers can be planted
in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if n flowers can be planted in the flowerbed without violating
        the no-adjacent-flowers rule.

        Parameters:
        - flowerbed: List[int] - array representing the garden (0 is empty, 1 is occupied)
        - n: int - number of new flowers to plant

        Returns:
        - bool - True if n flowers can be planted, False otherwise
        """
        # Optimization: If we don't need to plant any flowers, we are already done.
        if n == 0:
            return True

        length = len(flowerbed)

        for i in range(length):
            # We can only plant if the current plot is empty
            if flowerbed[i] == 0:
                
                # Check Left Neighbor: 
                # It is valid if we are at the first index (no left neighbor) 
                # OR if the previous plot is empty.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                # Check Right Neighbor:
                # It is valid if we are at the last index (no right neighbor)
                # OR if the next plot is empty.
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                # If the spot is valid on both sides, plant the flower
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Mark plot as occupied
                    n -= 1            # Decrement the count of flowers needed
                    
                    # If we have successfully planted all n flowers, return True immediately
                    if n == 0:
                        return True

        # If we exit the loop and still have flowers left to plant (n > 0), return False
        return n <= 0

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    print(f"Input: {flowerbed1}, n={n1}")
    print(f"Output: {solution.canPlaceFlowers(flowerbed1, n1)}") 
    # Output: True

    # Example 2
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    print(f"\nInput: {flowerbed2}, n={n2}")
    print(f"Output: {solution.canPlaceFlowers(flowerbed2, n2)}") 
    # Output: False
    
    # Example 3 (Edge Case: Start of array)
    flowerbed3 = [0, 0, 1]
    n3 = 1
    print(f"\nInput: {flowerbed3}, n={n3}")
    print(f"Output: {solution.canPlaceFlowers(flowerbed3, n3)}") 
    # Output: True