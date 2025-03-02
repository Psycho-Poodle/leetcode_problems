""" Problem:

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        max_length = max(len(word1), len(word2))
        
        for i in range(max_length):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return "".join(result)

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    solution = Solution()
    merge_string = solution.mergeAlternately(word1, word2)
    print(merge_string)  
