class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-w for w in stones]  # -vals in heap

        heapq.heapify(maxHeap)  # make it a maxHeap -vals

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            diff = y - x
            if y != x:
                heapq.heappush(maxHeap, -diff)
        
        if maxHeap:
            return -maxHeap[0]
        
        return 0

