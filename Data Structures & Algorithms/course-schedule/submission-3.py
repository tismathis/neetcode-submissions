class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses #counter to know how many prereq are left for each node if one of them is 0 then we can append our counter 
        adj = [[] for i in range(numCourses)]  #lists to know what are the edges of a certain node 

        finish = 0 

        for src,pre in prerequisites : 
            indegree[pre] +=1 
            adj[src].append(pre) #add to the list 

        q = deque() 
        for i in range(numCourses) : 
            if indegree[i] == 0 :
                q.append(i) 

        while q : 
            curr = q.popleft()
            finish +=1 
            for nodes in adj[curr] : 
                indegree[nodes] -=1
                if indegree[nodes] == 0:
                    q.append(nodes)
        return finish == numCourses 




         