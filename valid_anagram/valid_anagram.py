# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: fals


# from collections import Counter
# Create a dictionary in python using {} -> dic = {}
# Get from dictionary using -> example = dic.get(item, 0), where 0 is a default value if item not in dic
# Set a value in dictionary by doing -> dic[example] = 1
# Check if two dics are equal using == -> dic1 == dic2
# Solution: Create two dictionaries to store letters and count of letters in respective words, and check if the two dictionaries are equal. If they are equal, return True, else return False. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0): #that's how you access elements in hashmap
                return False            # c is the key here going through each letter
        return True
            


            




        