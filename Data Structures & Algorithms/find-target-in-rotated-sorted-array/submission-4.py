class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0 
        r = n - 1 

        while l < r:
            m = l + ((r-l) // 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 

        min_i = l

        if min_i == 0:
            l = 0 
            r = n - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l = 0
            r = min_i - 1
        else:
            l = min_i
            r = n - 1
        
        while l <= r:
            m = l + ((r-l) // 2)
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1 
            







        
        