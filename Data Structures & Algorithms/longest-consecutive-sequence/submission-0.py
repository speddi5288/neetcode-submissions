class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) # store as hashset -> O(1) lookup for unordered set
        longestSeq = 0     # Initialize longestConsectiveSequence output

        for n in nums:                  # Iterate through arr
            if (n-1) not in numSet:     # Check left neighbor for each num
                length = 0              # Init length of each seq to compare it later on
                while (n + length) in numSet:   # Check if right elts of seq exist 
                    length += 1                 # If they do inc the length 
                longestSeq = max(length, longestSeq)  # Store the bigger longestSeq

        return longestSeq




        