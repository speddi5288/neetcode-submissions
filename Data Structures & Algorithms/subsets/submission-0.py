class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            if i == n:         # ind out of bounds -> base case
                res.append(sol[:])      # append the copy of whatever is in sol
                return                  # index out of bounds -> skip
            
            # Dont pick nums[i]
            backtracking(i+1)


            # Pick nums[i]
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)
        return res