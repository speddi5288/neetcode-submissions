# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to serve as the head of the new merged list.
        # This simplifies edge cases and avoids special handling for the head node.
        dummy = ListNode()

        # Use a `current` pointer to build the new list.
        # It starts at the dummy node and moves forward as nodes are added.
        current = dummy

        # Loop while both lists have nodes to compare.
        while list1 and list2:
            if list1.val <= list2.val:
                # If list1's value is smaller, add it to the merged list
                current.next = list1
                # Move list1's pointer forward.
                list1 = list1.next
            else:
                # If list2's value is smaller, add it to the merged list.
                current.next = list2
                # Move list2's pointer forward.
                list2 = list2.next
            # Always move the `current` pointer forward to the newly added node.
            current = current.next

        # After the loop, one of the lists might still have remaining nodes.
        # Attach the remaining portion of the non-empty list to the end.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The first node of the merged list is `dummy.next`.
        # The dummy node itself is just a placeholder.
        return dummy.next



        