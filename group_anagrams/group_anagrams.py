# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]


# - In a regular dictionary, if you try to access or modify a key that doesn't exist, you get a KeyError.
# - With `defaultdict(list)`, if you try to access a key that doesn't exist, it automatically creates that key with a default value - in this case, an empty list. This simplifies our code by avoiding explicit checks for existing keys.

# List in python = [] -> list = []
# Add to list using .append(item) -> list.append(2)
# Solution: Initialize result dictionary, and list to store all possible dictionaries. Outer loop through all all words in strs. Initialize dic to store current words dictionary. Get dictionary of word. If dictionary not already in list of dictionaries, append dic to dictionaries list. Get index of dic in dictionaries, and get current array of words in result dictionary at that index. Append word to that array, and set this new array back to dictionary value at the index. Return dictionary values after looping through all words.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a .. z

            for c in s:
                count[ord(c) - ord("a")] += 1
            Map[tuple(count)].append(s)
        return list(Map.values())