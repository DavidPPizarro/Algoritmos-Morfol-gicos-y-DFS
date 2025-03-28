from collections import deque

class Grafo:
    def __init__(self):
        self.adyacencia = {}


    def agregar_arista(self, nodo1, nodo2):
        
        if nodo1 not in self.adyacencia:
            self.adyacencia[nodo1] = []
        if nodo2 not in self.adyacencia:
            self.adyacencia[nodo2] = []
        self.adyacencia[nodo1].append(nodo2)
        self.adyacencia[nodo2].append(nodo1)

    def get_neighbors(self, nodo):        
        return self.adyacencia.get(nodo, [])

def bfsDelGrafo(graph, start, end):
    queue = deque([[start]])  

    while queue:
        current_path = queue.popleft()  
        last_node = current_path[-1]  

        if last_node == end:  
            return current_path

        for next_vertex in graph.get_neighbors(last_node):
            if next_vertex not in current_path: 
                new_path = current_path + [next_vertex]
                queue.append(new_path)

    return None 

grafo = Grafo()
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(2, 5)
grafo.agregar_arista(3, 6)
grafo.agregar_arista(3, 7)
grafo.agregar_arista(5, 6)


origen, destino = 1, 6
camino = bfsDelGrafo(grafo, origen, destino)

if camino:
    print(f"Camino más corto de {origen} a {destino}: {camino}")
else:
    print(f"No hay camino entre {origen} y {destino}")

print(grafo.adyacencia)
