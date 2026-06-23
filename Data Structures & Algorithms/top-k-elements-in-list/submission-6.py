from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        freq = [ [] for i in range(len(nums) + 1) ]

        for n in nums:
            counter[n] = counter.get(n,0) + 1

        for key, val in counter.items():
            freq[val].append(key)

        res = []
        for i in range( len(freq) - 1, 0, -1 ):

            for n in freq[i]:   # use for loop since you are checking every elt IN THE LIST that is inside the list, not just one iteration
                res.append(n)
                if len(res) == k:
                    return res
        return res
            












        