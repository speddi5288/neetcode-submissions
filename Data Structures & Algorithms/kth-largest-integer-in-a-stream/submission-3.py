class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Init member vars
        self.minHeap = nums
        self.k = k
        
        # make the list into a minHeap
        heapq.heapify(self.minHeap)     # Time: O(n)

        # make the minheap size of k by removing smallest node (root)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)     # O(log n)
        
        # T: O(nlogn)
        # S: O(n)

    def add(self, val: int) -> int:
        # Push a given num into the heap
        heapq.heappush(self.minHeap, val)      # T: O(log n)
            # if heap is bigger than k, remove smallest elt
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)     # T: O(log n)
            # Return the root of the heap (will be kth biggest value) -> O(1) time

        return self.minHeap[0]

    # Time: O(logn) -> Overall O(nlogn) 
    # Space: O(n) -> Overall O(n)

        
