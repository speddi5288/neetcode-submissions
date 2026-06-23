from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev = {}                           # Create an empty map

        for ind, val in enumerate(nums):        # Automatically pairs each item with [i = index : n = value]

            diff = target - val              # the number we have to look for
            
            if diff in prev:
                return [ prev[diff], ind ]

            prev[val] = ind
        return



        