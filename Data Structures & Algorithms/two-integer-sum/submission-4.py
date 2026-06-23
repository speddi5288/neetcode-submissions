from collections import defaultdict

    # Input: nums = [3,4,5,6], target: 7
    # Output: Index (i) and index(j) whose values add up to target
    # [0,1]
    # nums[0] + nums[1] == 7


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = defaultdict(int)
        # key = val : value = index

        for i, j in enumerate(nums):
            diff = target - j       # 7 - j(4) = 3: diff
            if diff not in my_map:
                my_map[j] += i      # key: 3, val: 0
            else:                   # my_map {, 1:4, }
                return [my_map[diff], i]        










        
        