"""
1351. Count Negative Numbers in a Sorted Matrix (Easy)
Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Problem:
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.

Example:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

---
My Approach:
Iterate through each row. Since rows are sorted non-increasingly, 
once we hit a negative number, ALL subsequent numbers in that row are also negative.
We add the remaining count and break to the next row.

Time Complexity: O(m * n) - Worst case we traverse all elements (e.g. all positive).
Space Complexity: O(1) - No extra space used.
"""

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        number_negative = 0
        number_rows = len(grid)
        number_columns = len(grid[0])

        for row in grid:
            # We track how many columns are left to check
            columns_left = number_columns
            
            for column in row:
                if column < 0:
                    # Found a negative. Since it's sorted, ALL remaining are negative.
                    # Add remaining count and stop checking this row.
                    number_negative += columns_left
                    break
                
                # Decrement because we checked one positive number
                columns_left -= 1
        
        return number_negative

# Unit Test (Optional but Pro)
if __name__ == "__main__":
    sol = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(f"Test Case 1: {sol.countNegatives(grid)}") # Expected: 8
    
"""
Alternative Optimization Strategy (Mental Model):
Start at Top-Right (row=0, col=last).
- If grid[row][col] is Negative:
    Since columns are sorted descending, all rows below this are also negative.
    Add (total_rows - current_row) to count.
    Move Left (col -= 1).
- If grid[row][col] is Positive:
    We need smaller numbers.
    Move Down (row += 1).
    
This reduces Time Complexity from O(m*n) to O(m+n).
"""