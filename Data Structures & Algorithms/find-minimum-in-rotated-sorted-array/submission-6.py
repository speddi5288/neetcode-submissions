class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else: # nums[m] <= nums[r]
                r = m
            
        # Time: O(log n)
        # Space: O(1)
        return nums[l]