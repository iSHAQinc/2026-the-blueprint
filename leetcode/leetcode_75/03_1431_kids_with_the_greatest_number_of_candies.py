"""
LeetCode Problem 1431: Kids With the Greatest Number of Candies
Difficulty: Easy

Problem:
There are n kids with candies. You are given an integer array 'candies', where
candies[i] represents the number of candies the i-th kid has, and an integer
'extraCandies', denoting the number of extra candies you have.

Return a boolean array 'result' of length n, where result[i] is True if, after
giving the i-th kid all the extraCandies, they will have the greatest number of
candies among all the kids, or False otherwise.

Example:
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
Output: [True, True, True, False, True]
Explanation: 
- Kid 1: 2 + 3 = 5 → greatest among kids? Yes → True
- Kid 2: 3 + 3 = 6 → Yes → True
- Kid 3: 5 + 3 = 8 → Yes → True
- Kid 4: 1 + 3 = 4 → No → False
- Kid 5: 3 + 3 = 6 → Yes → True
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determines which kids can have the greatest number of candies
        after receiving all the extraCandies.

        Parameters:
        - candies: List[int] - number of candies each kid has
        - extraCandies: int - number of extra candies available

        Returns:
        - List[bool] - list of booleans indicating if each kid can have the greatest number
        """
        result = []

        # Find the current maximum number of candies among all kids
        greatest = max(candies)

        # Check for each kid if giving them all extraCandies makes them have the greatest
        for kid in candies:
            if kid + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(solution.kidsWithCandies(candies, extraCandies))
    # Output: [True, True, True, False, True]

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(solution.kidsWithCandies(candies, extraCandies))
    # Output: [True, False, False, False, False]
