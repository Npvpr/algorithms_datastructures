class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # this method is not true for all inputs
        # This is incorrect when the number of graph is odd and looped all around(meaning: last node and first node are connected)
        for first_list in graph:
            for second_index in first_list:
                second_list = graph[second_index]
            
            if len(first_list) > len(second_list):
                for first_element in first_list:
                    if first_element in second_list:
                        return False
            else:
                for second_element in second_list:
                        if second_element in first_list:
                            return False
        return True