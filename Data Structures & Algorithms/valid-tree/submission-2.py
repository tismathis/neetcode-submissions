class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited_nodes = set()

        for i,j in edges : 
            if i in visited_nodes and j in visited_nodes : 
                return False 
            if i not in visited_nodes and j not in visited_nodes :
                return False 
            visited_nodes.add(i)
            visited_nodes.add(j)
        return True 