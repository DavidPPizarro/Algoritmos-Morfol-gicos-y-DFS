from collections import deque #permite insertar y eliminar elementos en ambos extremos de una cola lineal

def bfs(grafo, inicio_nodo):
    visitado = set()  # GUARDAR TEMPORALMENTE NODOS
    queue = deque([inicio_nodo])  # Inicializamos la cola con el nodo inicial

    while queue:
        node = queue.popleft()  # Sacamos el primer nodo de la cola (FIFO)
        if node not in visitado: #Verificamos si ya hemos visitado el nodo
            print(node, end=" ")  
            visitado.add(node)  # Marcamos como visitado
            queue.extend(grafo[node])  # Agregamos sus vecinos no visitados a la cola

# Definimos un grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['E', 'B'],
    'B': ['F', 'H'],
    'E': ['D', 'L'],
    'D': [],
    'L': [],
    'F': [],
    'H': []
}

# Llamamos a BFS desde el nodo 'A'
bfs(grafo, 'E')