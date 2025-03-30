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
        if node is None:
            return node

        old_visited = set()
        new_created = set()
        new_root = None
        queue = deque([node])

        while queue:
            cur_old_node = queue.popleft()
            if cur_old_node not in old_visited:
                cur_new_node = None
                for new_node in new_created:
                    if cur_old_node.val == new_node.val:
                        cur_new_node = new_node
                if cur_new_node == None:
                    cur_new_node = Node(cur_old_node.val)
                    if len(new_created) == 0:
                        new_root = cur_new_node
                    new_created.add(cur_new_node)
                old_visited.add(cur_old_node)
                
                                
                for old_neighbor in cur_old_node.neighbors:
                    cur_new_neighbor = None
                    for new_node in new_created:                        
                        if old_neighbor.val == new_node.val:
                            cur_new_neighbor = new_node
                    if cur_new_neighbor == None:
                        cur_new_neighbor = Node(old_neighbor.val)
                        new_created.add(cur_new_neighbor)
                    cur_new_node.neighbors.append(cur_new_neighbor)
                    queue.append(old_neighbor)
                    
        print(new_root)
        # print(new_root.neighbors)

        for i in old_visited:
            print("old_visited: ", i.val)

        for i in new_created:
            print("new_create: ", i.val)
        # print(new_created)
        
        return new_root
        