from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = defaultdict(int)
        for x in nums:
            count[x] += 1

        # Buckets: freq -> list of numbers with that freq
        buckets = defaultdict(list)
        max_freq = 0
        for num, c in count.items():
            buckets[c].append(num)
            if c > max_freq:
                max_freq = c

        # Collect from highest freq down
        res = []
        for f in range(max_freq, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res

        return res