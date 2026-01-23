# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# To get max value from a list use max() -> maxVal = max(exampleList)
# To remove a value from a list use .remove(value) -> exampleList.remove(1)
# Solution: Create a dic to store count of all values, and populate this dictionary. Then store the keys and values into two lists respectively. For i in range 0->k, get the max element from the values dictionary (max count) and the index of this item in the list. This is where the ith most frequent item will show up in the keys list, so get that item and append it to the result list. Remove both the max count from values and the item from keys, return result at end of loop.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        count = {}
        freq = [[] for i in range (len(nums)+ 1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
    # time complexity: o(n + n) becomes o(n)