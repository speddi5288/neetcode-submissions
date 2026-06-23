# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if not root: return None

        inverted_left = self.invertTree(root.left)

        inverted_right = self.invertTree(root.right)

        # Swap the inverted subtrees, og left = right and vice versa
        root.left = inverted_right
        root.right = inverted_left

        return root
