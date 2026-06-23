from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        freq = [ [] for i in range(len(nums) + 1) ]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, c in counter.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result











        