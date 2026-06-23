class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        remove_dupes = set(nums)

        if len(remove_dupes) == len(nums):
            return False
        
        return True

        


        # [1,2,3,3]