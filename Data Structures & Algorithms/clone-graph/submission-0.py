"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copy = {}
        copy[node] = Node(node.val)
        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()
            for neib in curr_node.neighbors:
                if neib not in copy:
                    copy[neib] = Node(neib.val)
                    queue.append(neib)
                copy[curr_node].neighbors.append(copy[neib])
        return copy[node]