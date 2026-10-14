class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(i):
            visited.add(i)              # marquer AVANT d'explorer
            for j in adj[i]:
                if j not in visited:
                    dfs(j)

        counter = 0
        for i in range(n):
            if i not in visited:        # nouveau point de départ = nouvelle composante
                counter += 1
                dfs(i)

        return counter