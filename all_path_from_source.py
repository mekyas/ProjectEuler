from typing import List

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        def dfs(graph, result, path, u):
            path.append(u)
            if u== len(graph)-1:
                result.append(path.copy())
            else:
                for elt in graph[u]:
                    dfs(graph, result, path, elt)
            path.pop()
        dfs(graph, result, path, 0)
        return result

print(allPathsSourceTarget([[1,2], [3], [3], []] ))