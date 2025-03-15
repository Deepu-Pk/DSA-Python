"""
    Graph data structure implementation
"""
from collections import deque

class Graph:
    def __init__(self,gdict : dict):
        if(gdict is None):
            gdict = {} 
        self.gdict = gdict 
    

    def addEdge(self,vertex : str, edge : str):
        """
            Adding new vertex into graph
        """
        self.gdict[vertex].append(edge) 

    def bfs(self,vertex : str) -> None:
        """
            Breadth first algorithm
        """ 
        visited : list = []
        q = deque([vertex]) 
        while(q):
            node = q.popleft()
            if node not in visited:
                visited.append(node)
                print(f"{node} ->",end = " ")
                for nbr in self.gdict[node]:
                    q.append(nbr)


    

    def dfs(self,vertex : str) -> None: 
        """
            Depth first algorithm
        """
        visited : list = [] 
        s : list = [] 
        s.append(vertex) 
        while(s):
            node = s.pop()
            if node not in visited:
                visited.append(node)
                print(f"{node} ->",end = " ")
                for nbr in self.gdict[node]:
                    s.append(nbr)


if(__name__ == "__main__"): 
    gdict = {
        'A' : ['B','C'],
        'B' : ['A','D','E'],
        'C' : ['A','E'],
        'D' : ['B','E'], 
        'E' : ['B','C'], 
        'F' : ['B','E']
    }

    graph = Graph(gdict)
    print(f"Graph : {graph.gdict}")
    print()
    graph.addEdge('E','D')
    print(f"Graph adding E edge {graph.gdict}")
    print(f"Breadth first search : ",   end = " ")
    graph.bfs('A') 
    print()
    print(f"Depth first search  : ",end = " ")
    graph.dfs("A")
    print()