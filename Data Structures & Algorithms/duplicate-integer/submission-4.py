class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create a set to store seen elements
        for num in nums:  # Iterate through the array
            if num in seen:  # If the element is already in the set
                return True  # Return True (duplicate found)
            seen.add(num)  # Add the element to the set
        return False  # If no duplicates are found, return False

