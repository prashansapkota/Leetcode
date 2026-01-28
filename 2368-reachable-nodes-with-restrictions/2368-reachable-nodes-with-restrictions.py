class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visited = set()
        count = 0
        restricted = set(restricted)
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(root):
            if root in visited or root in restricted:
                return
            
            visited.add(root)
            for neighbor in graph[root]:
                dfs(neighbor)
        
        dfs(0)
        return len(visited)
            
            
        