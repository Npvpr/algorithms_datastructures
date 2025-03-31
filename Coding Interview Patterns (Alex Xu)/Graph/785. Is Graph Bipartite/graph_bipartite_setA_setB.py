class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            
        setA = set()
        setB = set()
        visited = set()

        iteration = 0
        queue = deque([])

        # if graph[index] list is not empty, process queue
        # if empty or visited, go to next index
        for index in range(len(graph)):
            if graph[index] and index not in visited:
                queue.append(index)
                while queue:
                    for _ in range(len(queue)):
                        value = queue.popleft()
                        if iteration % 2 == 0:
                            setA.add(value)
                        if iteration % 2 != 0:
                            setB.add(value)
                        if value not in visited:                   
                            for adjacent in graph[value]:
                                queue.append(adjacent)
                            visited.add(value)
                    iteration += 1
        
        print("setA: ", setA)
        print("setB: ", setB)
        if len(setA) > len(setB):
            for i in setA:
                if i in setB:
                    return False
        else:
            for i in setB:
                if i in setA:
                    return False

        return True