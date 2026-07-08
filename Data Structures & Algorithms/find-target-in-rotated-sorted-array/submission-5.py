class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l

        if min_index == 0:      # edge case for normal BS
            l, r = 0, len(nums) - 1

        # checking if target num in the left partition
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        # target is in right partition
        else:
            l, r = min_index, len(nums) - 1
        
        # now BS through from any of those three starting pts
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1       # if not found


            