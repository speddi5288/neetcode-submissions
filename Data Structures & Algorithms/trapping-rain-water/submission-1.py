class Solution:
    def trap(self, height: List[int]) -> int:

        # O(n space): Prefix and Suffix Array

        n = len(height)     # height length

        if n == 0:          # Empty arr -> no water can be trapped
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]  #put 1st val from heights arr into the leftMax list

        # 1-based indexing, to n (exclusive), since first val alr in leftMax
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])   # choose largest val in  arr and put it in maxLeft Array in correct pos
        
        rightMax[n - 1] = height[n - 1] # start rightMax leftmost val with height leftmost val
        
        for i in range(n - 2, -1, -1):  # start @ 2nd to last index, go until last index(0) & step backwards
            rightMax[i] = max(rightMax[i+1], height[i]) # same as leftMax array but backwards
        

        res = 0     # init res
        for i in range(n): #1->11       # loop through len of height list
            res += min(leftMax[i], rightMax[i]) - height[i]     # add res to min of largest l and r at respective pos and subtract with current height(black boxes) to get water trapped at each pos and return res to get total amt of water that was trapped 
        return res




        

        