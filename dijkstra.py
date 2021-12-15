from collections import defaultdict
import heapq

# Graph class for Dijkstra's algorithm
class Graph:
    def __init__(self, n, m):
        self.nodes = {(x,y) for x in range(n) for y in range(m)}
        self.edges = defaultdict(list)
        self.distances = {}
        
    def add_edge(self, node1, node2, distance):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)
        self.distances[(node1, node2)] = distance
        self.distances[(node2, node1)] = distance
        
def dijkstra(graph:Graph, start:tuple, end:tuple):
    # Set up the priority queue
    queue = [(0, start)]
    visited = set()
    # Keep track of the distances
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    while queue:
        # Get the node with the smallest distance
        _, node = heapq.heappop(queue)
        # If we've already visited this node, skip it
        if node in visited:
            continue
        visited.add(node)
        # If we've found the end node, we're done
        if node == end:
            break
        # Otherwise, add the edges to the queue
        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                distance = distances[node] + graph.distances[(node, neighbor)]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
    return distances[end]

def path_finder(area:str):
    grid = area.split('\n')
    maze = Graph(len(grid), len(grid[0]))
    i,j = 0,0
    while i < len(grid):
        while j < len(grid[i])-1:
            distance = abs(int(grid[i][j]) - int(grid[i][j+1]))
            maze.add_edge((i,j), (i,j+1), distance)
            j += 1
        j = 0
        i += 1
    i,j = 0,0
    while i < len(grid)-1:
        while j < len(grid[i])-1:
            distance = abs(int(grid[i][j]) - int(grid[i+1][j]))
            maze.add_edge((i,j), (i+1,j), distance)
            j += 1
        j = 0
        i += 1
    return dijkstra(maze, (0,0), (len(grid)-1,len(grid[0])-1))

d = "\n".join([
"8128",
"3355",
"6341",
"8851"
])

print(path_finder(d))