# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        1) Use slow and fast ptrs to find middle of list
        2) When middle is found anything on 2nd half must be reversed
        3) Merge the lists in the given order.
        '''

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # starting of 2nd half is slow.next
        second = slow.next
        # break link between 1st half andd 2nd half (avoids cycles)
        slow.next = None
        
        # reverse the list
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev is now head of 2nd half of list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2



