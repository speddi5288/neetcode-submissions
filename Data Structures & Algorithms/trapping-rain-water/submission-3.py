class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        cur_max = 0
        for h in height:
            cur_max = max(cur_max, h)
            prefix.append(cur_max)
        
        suffix = []
        current_max = 0 
        for i in range(len(height)-1 , -1, -1):
            current_max = max(current_max, height[i])
            suffix.append(current_max)
        suffix.reverse()

        water = 0 
        for i in range(len(height)):
            water += (min(prefix[i], suffix[i]) - height[i])

        return water 