class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp = {}

        for i, n in enumerate(nums):
            numtofind = target - n
            if numtofind in mapp:
                return [mapp[numtofind], i]
            mapp[n] = i
            
