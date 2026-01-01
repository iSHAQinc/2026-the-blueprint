"""
1071. Greatest Common Divisor of Strings (Easy)
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

Problem:
For two strings str1 and str2, find the largest string x such that x divides both str1 and str2.
A string t divides s if s = t + t + ... + t (one or more times).

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

---
My Approach:
1. Check compatibility: if str1 + str2 != str2 + str1, no common divisor exists.
2. Compute the GCD of the lengths of str1 and str2. This gives the maximum possible length for x.
3. Slice the first g characters from str1 as candidate x.
4. Verify that repeating x can reconstruct both str1 and str2 exactly.

Time Complexity: O(n + m) - n and m are lengths of str1 and str2. 
Space Complexity: O(n + m) if building repeated strings manually; can be optimized using string multiplication.
"""

def gcd(a, b):
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a

def divides(x, s):
    # Check if x repeated makes s exactly
    if len(s) % len(x) != 0:
        return False
    times = len(s) // len(x)
    repeated = ""
    for _ in range(times):
        repeated += x  # Build repeat manually
    return repeated == s

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check compatibility
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Get GCD length
        g = gcd(len(str1), len(str2))
        
        # Step 3: Candidate x
        x = str1[:g]  # Slice first g chars
        
        # Step 4: Verify (optional but good)
        if divides(x, str1) and divides(x, str2):
            return x
        return ""

# Unit Test (Optional but Pro)
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("ABCABC", "ABC"),
        ("ABABAB", "ABAB"),
        ("LEET", "CODE"),
        ("AAAAAB", "AAA"),
    ]
    for i, (s1, s2) in enumerate(test_cases, 1):
        print(f"Test Case {i}: {sol.gcdOfStrings(s1, s2)}")
