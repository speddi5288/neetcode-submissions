class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0 
        r = n - 1

        # Stop when pointers meet at the single smallest element
        while l < r:
            m = l + ((r - l) // 2)

            # If mid is greater than right, the drop (min) is to the right
            if nums[m] > nums[r]:
                l = m + 1
            
            # If mid is smaller/equal, the min is here or to the left
            else:
                r = m
    
        return nums[l]