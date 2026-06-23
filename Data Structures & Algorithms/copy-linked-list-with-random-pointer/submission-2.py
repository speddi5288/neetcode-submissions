"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        newList = {}

        curr = head
        while curr:
            newList[curr] = Node(curr.val)
            curr = curr.next
    
        curr = head
        while curr:
            copy = newList[curr]
            copy.next = newList.get(curr.next)
            copy.random = newList.get(curr.random)
            curr = curr.next
        return newList.get(head)



