class Graph:
      
    adj = []
  
    # Llenar la matriz adjacente
    def __init__(self, v, e):
          
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)] 
                        for j in range(v)]
  
    # Agregar arista
    def addEdge(self, start, e):
          
        # Agregar arista bidireccional
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
  
    # DFS en el grafo
    def DFS(self, start, visited):
          
        #Imprimir nodo actual
        print(start, end = ' ')
  
        #Marcar como visitado
        visited[start] = True
  
        # Por cada nodo en el grafo
        for i in range(self.v):
              
            # Si un nodo es adjacente al nodo actual, y no esta marcado
            if (Graph.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)
  
# Driver code
v, e = 5, 4
  
# Crear el Grafo
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(0, 3)
G.addEdge(0, 4)
  

#Vector ya visitado, para evitar que se repitan
visited = [False] * v
  
# DFS
G.DFS(0, visited);
