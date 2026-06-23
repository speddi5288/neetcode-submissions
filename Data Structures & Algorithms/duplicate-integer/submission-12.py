class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sett = set(nums)        # {1,2,3}
        
        if len(sett) != len(nums):
            return True
            
        return False

        