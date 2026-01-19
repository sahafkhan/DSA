# Get index of an element in a list using .index() -> fruits.index(“apple”)
# Slicing list in python: new_list = original_list[start:end:step]
# start: The index at which the slicing should begin (inclusive).
# end: The index at which the slicing should end (exclusive).
# step: The increment value for selecting elements (optional).
# Solution: For i in range len(nums), calculate total - current number. If that remainder is in the rest of the list (nums[i+1:], return i and the index of the second number (nums[i+1].index(remainder) + i + 1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Map = {}, #val, index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in Map:
                return [Map[difference], i]
            Map[n] = i
        
        return
        