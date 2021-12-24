from MST import MST
from heap import heap

inf = 1000000000

def heuristic(graph, unvisited_cities, curr, start):
    weight = 0

    mn = (inf, -1)  # distance to the nearest unvisited city from the current city
    for i in range(len(graph)):
        if unvisited_cities[i]:
            if graph[curr][i] < mn[0]:
                mn = (graph[curr][i], i)
    if mn[1] != -1:
        weight += mn[0]

    mst = MST(graph, unvisited_cities)  # estimated distance to travel all the unvisited cities (MST heuristic used
    tree = mst.getMST()  # here)
    for i in tree:
        weight += i[0]

    mn = (inf, -1)  # nearest distance from an unvisited city to the start city
    for i in range(len(graph)):
        if unvisited_cities[i]:
            if graph[start][i] < mn[0]:
                mn = (graph[start][i], i)

    if mn[1] != -1:
        weight += mn[0]

    return weight


def TSP(graph, start=0):
    n = len(graph)

    priority_queue = heap("min")
    unvisited_nodes = [True for _ in range(n)]
    unvisited_nodes[start] = False
    path = [start]
    fx = 0 + heuristic(graph, unvisited_nodes, start, start)  # gx + hx
    priority_queue.push((fx, path, unvisited_nodes))
    min_path = []
    min_dis = inf
    total_states_visited = 0
    while not priority_queue.isEmpty():
        total_states_visited += 1
        curr = priority_queue.pop()
        dis = curr[0]
        path = curr[1]
        node = path[-1]
        unvisited_nodes = curr[2]
        if len(path) >= n + 1:
            min_path = path
            min_dis = dis
            break
        if len(path) == n:
            unvisited_nodes[path[0]] = True
        for i in range(n):
            if unvisited_nodes[i]:
                new_path = path.copy()
                new_unvisited_nodes = unvisited_nodes.copy()
                new_path.append(i)
                new_unvisited_nodes[i] = False

                gx = 0
                for j in range(1, len(new_path)):
                    gx += graph[new_path[j - 1]][new_path[j]]

                fx = gx + heuristic(graph, new_unvisited_nodes, i, path[0])  # fx = gx + hx
                priority_queue.push((fx, new_path, new_unvisited_nodes))

    print(*(i for i in min_path), sep=" -> ")
    print("Minimum distance : ", min_dis)

matrix = []
n = int(input())
# For user input
for i in range(n):  # A for loop for row entries
    a = list(map(int, input().split()))
    matrix.append(a)
TSP(matrix)
