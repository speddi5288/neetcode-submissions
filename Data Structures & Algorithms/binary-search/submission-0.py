class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0                       # Left is the index of 0
        R = len(nums) - 1           # Gives the last element in the arr (called nums)

        while(L <= R): 
            M = (L + R) // 2            # Gives us the middle postion

            if (nums[M] == target):       # If the value in the middle postion is equal to the target, we will return the index
                return M;

            if (target > nums[M]):
                L = M + 1;
            else:
                R = M - 1;

        return -1;
        

