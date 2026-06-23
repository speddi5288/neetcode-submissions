class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val : index

        for pos, val in enumerate(nums):    # position (i) & value (n)

            diff = target -  val

            if diff in prevMap:
                return [prevMap[diff], pos]

            prevMap[val] = pos



        