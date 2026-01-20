# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#         Contains Duplicate: 
# Sort a list in python with .sort()
# Use set() for unique values, and .add to add new values -> exampleList = set()
# Solution: Use set to keep track of seen numbers, if a num in nums is in seen, return True since duplicate. Else add that num to seen numbers, return false if all nums are unique. 

        #hashset solution
        Map = set()

        for n in nums:
            if n in Map:
                return True
            Map.add(n)
        return False   
        # time complexity o(n), space complexity o(n)


        #brute force
        # for i in range (len(nums)):
        #     for j in range (i + 1 , len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
                
        # return False


                
        