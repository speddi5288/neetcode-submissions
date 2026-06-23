class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        removeDupes = set(nums)

        if len(nums) != len(removeDupes):
            return True
        
        return False
        