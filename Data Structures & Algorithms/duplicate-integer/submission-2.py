class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):  # Outer loop: pick the current element
            for j in range(i + 1, len(nums)):  # Inner loop: compare with the rest of the elements
                if nums[i] == nums[j]:  # If a duplicate is found
                    return True  # Return True
        return False  # If no duplicates are found, return False

