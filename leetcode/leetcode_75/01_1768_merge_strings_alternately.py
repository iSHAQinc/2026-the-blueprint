"""
1768. Merge Strings Alternately
Easy

This file contains a Python solution to the "Merge Strings Alternately" problem.
Given two strings, merge them by alternating characters. If one string is longer,
append the remaining characters at the end.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately starting with word1.

        Args:
            word1 (str): The first string.
            word2 (str): The second string.

        Returns:
            str: The merged string.
        """
        merged_chars = []

        # Step 1: loop up to the length of the shorter string
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            merged_chars.append(word1[i])
            merged_chars.append(word2[i])

        # Step 2: append leftover characters from the longer string
        if len(word1) > len(word2):
            merged_chars.extend(word1[min_len:])
        elif len(word2) > len(word1):
            merged_chars.extend(word2[min_len:])

        # Step 3: join list into final string
        return "".join(merged_chars)

        # Note: In Python, a more concise approach could use zip:
        # for c1, c2 in zip(word1, word2):
        #     merged_chars.append(c1)
        #     merged_chars.append(c2)
        # Even when using zip, you still need an if-statement (or slice) 
        # to handle leftover characters from the longer string.

# ------------------ TESTS ------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test examples from problem description
    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),         # edge case: first string empty
        ("hello", "", "hello"),     # edge case: second string empty
        ("a", "b", "ab"),           # minimal length strings
    ]

    for w1, w2, expected in test_cases:
        result = solution.mergeAlternately(w1, w2)
        print(f"mergeAlternately({w1!r}, {w2!r}) = {result!r} | Expected: {expected!r}")
        assert result == expected, f"Test failed for inputs: {w1}, {w2}"

    print("All tests passed!")
