import heapq
import time

start_time = time.time()

def readMaze(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            row = [c for c in line.strip()]
            maze.append(row)
    maze.remove(maze[0])
    return maze
    
def getStartEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                end = (i, j)
    return start, end

def getNeighbors(maze, node):
    neighbors = []
    for dx, dy, direction in [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != '%':   #changed '#' to '%'
            neighbors.append((x, y, direction))
    return neighbors
# movement

def ucs(maze):
    start, end = getStartEnd(maze)
    heap = [(0, start, "")]
    visited = set()
    c =[]
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == end:
            print('The cost is: ' + str(cost))
            return "The path is: " + path
        if node in visited:
            continue
        c.append(node)
        if range(len(c))== 1:
            pass
        elif len(c) >= 2 and c[-1][0] == c[-2][0] and c[-1][1] == c[-2][1]- 1:
            move = "left"
        elif len(c) >= 2 and c[-1][0] == c[-2][0] and c[-1][1] == c[-2][1]+ 1:
            move = "right"
        elif len(c) >= 2 and c[-1][0] == c[-2][0]-1 and c[-1][1] == c[-2][1]:
            move = "up"
        elif len(c) >= 2 and c[-1][0] == c[-2][0]+1 and c[-1][1] == c[-2][1]:
            move = "down"
        visited.add(node)
        for neighbor in getNeighbors(maze, node):
            heapq.heappush(heap, (cost + 1, neighbor[:2], path + neighbor[2]))
        print(c)
    return c

file_path = input("Enter the file path: ")
maze = readMaze(file_path)
print(ucs(maze))

end_time = time.time()
elapsed_time = end_time - start_time
print("runtime: " + str(elapsed_time))

print ("\nMaedeh Zarei \nMelika Khosravi \nFahimeh HassanZadeh \nMahdieh Mortezaie")
