# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:        # null lists or len of lists is 0
            return None
        
        # take pairs of ll's and merging them tg, and continue until 1 ll remains
        while len(lists) > 1:   # keep cutting list amount in half
            mergedLists = []     # new list for storage
            
            # iterate through the lists
            for i in range(0, len(lists), 2):       # want to do pairs (skip by 2)
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None     # check if l2 in bounds
                
                # take 2 lists and merge tg w/ helper func.
                # append them to mergedLists []
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    # merge two lists
    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
    
        return dummy.next