# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()          # dummy node, val 0 , next none
        dummy.next = head           # connect dummy to head of linked list
        behind = ahead = dummy      # both A & B point to dummy node

        for _ in range(n+1):        # wildcard since we dont need var and move A to 0->n+1 exclusive
            ahead = ahead.next
        
        while ahead:            # move ptrs until A goes out of bounds
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next      # skip (nth) node

        return dummy.next       # head location in case we dont have head (3 nodes each case, n = 3)
        