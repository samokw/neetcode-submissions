# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root] # Add the start none to the stack

        while stack:
            curr = stack.pop() # Pop the node
            curr.left, curr.right = curr.right, curr.left # Swap the children
            # If the swapped children exist add them to the stack
            if curr.left: 
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root