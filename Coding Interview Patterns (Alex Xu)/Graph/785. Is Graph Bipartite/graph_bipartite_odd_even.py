class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # this method is not correct for all cases
        # only correct if the value and index are the same, and if the even and odd numbers are not in the same set
        for index in range(len(graph)):
            # odd
            if index % 2 != 0:
                for element in graph[index]:
                    if element % 2 != 0:
                        return False
            # even
            if index % 2 == 0:
                for element in graph[index]:
                    if element % 2 == 0:
                        return False
        return True
