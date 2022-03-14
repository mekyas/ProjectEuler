from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create an adjacency list
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [False for _ in range(numCourses)]
        ordering = [0 for _ in range(numCourses)]
        i = numCourses - 1 
        def dfs(i, edge, visited, ordering, graph):
            from_edge = graph[edge]
            for e in from_edge:
                if not visited[e]:
                    dfs(i, e, visited, ordering, graph)
            ordering[i] = edge
            visited[edge] = True
            i -=1
                    
        for j in range(numCourses):
            edges = graph[j]
            for edge in edges:
                i = dfs(i, edge, visited, ordering, graph)
        return ordering

print(findOrder(2, [[1, 0]]))