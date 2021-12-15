import heapq, math
from typing import List

class Node:
    def __init__(self, position, parent, w=0):
        self.position = position
        self.parent = parent
        self.w = w
        self.g = 0
        self.h = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
    def __eq__(self, other):
        if type(other) is Node:
            return self.position == other.position
        elif type(other) is tuple:
            return self.position == other
    def __repr__(self):
        return str(self.position)
    def __hash__(self):
        return hash(self.position)
    
# Function takes 3 tuples, current postion, next postion and goal postion. Retuns true if next position is closer to goal postion than current position. Else returns false.
def is_closer(current:tuple, next:tuple, goal:tuple):
    return getHeuristic(next, goal) < getHeuristic(current, goal)
    
def aStar(start:tuple, goal:tuple, grid:List[str]):
    openSet = []
    closedSet = set()
    heapq.heappush(openSet, Node(start, None, w= int(grid[start[0]][start[1]])))
    while openSet:
        current:Node = heapq.heappop(openSet)
        if current.position == goal:
            path = []
            diff = 0
            while current.parent is not None:
                diff += abs(current.w)
                path.append(current.position)
                current = current.parent
            path.append(current.position)
            #print('Total distance:', diff)
            return diff
            #return path[::-1]
        closedSet.add(current)
        for neighbor in getNeighbors(current.position, grid):
            if neighbor in closedSet:
                continue
            neighborNode = Node(neighbor, current)
            neighborNode.w = abs(int(grid[neighbor[0]][neighbor[1]]) - int(grid[current.position[0]][current.position[1]]))
            neighborNode.g = current.g + 1
            neighborNode.h = getHeuristic(neighbor, goal)
            neighborNode.f = neighborNode.g + neighborNode.h + neighborNode.w
            if neighborNode not in openSet:
                heapq.heappush(openSet, neighborNode)
    return None

# only 4 directions: up, down, left, right
def getNeighbors(position:tuple, grid:List[str]):
    x, y = position
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < len(grid)-1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < len(grid[0])-1:
        neighbors.append((x, y+1))
    return neighbors

def getHeuristic(position:tuple, goal:tuple):
    return math.sqrt((position[0]-goal[0])**2 + (position[1]-goal[1])**2)

def print_path(path:tuple, maze:List[str]):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print('*', end='')
            else:
                print(maze[i][j], end='')
        print()

def path_finder(area:str):
    maze = area.split('\n')
    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)
    #path = aStar(start, end, maze)
    #print_path(path, maze)
    return aStar(start, end, maze)
    