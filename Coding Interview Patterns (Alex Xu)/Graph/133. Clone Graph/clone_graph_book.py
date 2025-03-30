"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        return self.dfs(node) 

    def dfs(self, node, clone_map = {}):
        if node in clone_map:
            return clone_map[node]
        cloned_node = Node(node.val)
        clone_map[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor, clone_map)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node
        