class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val : index
        
        for i, n in enumerate(nums): # gets both position (i) & value (n)
            diff = target - n        # creates the number to look for in map
            if diff in prevMap:      # check the diff is in the map
                return [prevMap[diff], i]   # return the indicies pairs that were used for target
            prevMap[n] = i           # If not in map add curr val in map

