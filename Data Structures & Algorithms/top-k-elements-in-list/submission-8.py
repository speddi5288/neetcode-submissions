class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [ [] for i in range(len(nums) + 1) ]
        #  0  1  2  3  4  5  6
        # [[],[],[],[],[],[],[]]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # count = {1:1, 2:2, 3:3}
        #          n,c

        for n, c in count.items():
            bucket[c].append(n)
        #  0   1   2   3  4  5  6
        # [[],[1],[2],[3],[],[],[]]
        #              ^

        ans = []
        for i in range(len(bucket) -1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        # ans = [3,2]
        
        return -1




        