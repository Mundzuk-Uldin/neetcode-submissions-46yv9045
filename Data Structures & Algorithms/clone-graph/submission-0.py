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
        dic = {}
        def addNode(node):
            if node.val in dic:
                return dic[node.val]
            newNode = Node(node.val)
            dic[newNode.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(addNode(neighbor))
            return newNode
        return addNode(node)