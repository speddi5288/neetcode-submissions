from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        result = []
        while k > 0:
            max_key = max(counter, key=counter.get)
            result.append(max_key)
            counter.pop(max_key)
            k -= 1
        return result

