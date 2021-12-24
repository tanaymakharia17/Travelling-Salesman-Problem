from MST import MST


finl = []
def dfs(tree, v, par):
    finl.append(v)
    if len(tree[v]) == 1 and tree[v][0][0] == par:
        return

    for edge in tree[v]:
        weight = edge[1]
        n = edge[0]
        if par == n:
            continue
        dfs(tree, n, v)
    return

def TSP(graph):
    n = len(graph)
    mst = MST(graph, [True] * n)
    edges = mst.getMST()
    tree = [[] for i in range(n)]
    for edge in edges:
        weight = edge[0]
        n1 = edge[1][0]
        n2 = edge[1][1]
        tree[n1].append((n2, weight))
        tree[n2].append((n1, weight))
    finl.clear()
    dfs(tree, 0, -1)
    finl.append(0)
    dis = 0
    for i in range(1, len(finl)):
        dis += graph[finl[i]][finl[i-1]]
    print(*finl, sep=" -> ")
    print("Minimum distance with MST : ", dis)

matrix = []

n = int(input())
# For user input
for i in range(n):  # A for loop for row entries
    a = list(map(int, input().split()))
    matrix.append(a)
TSP(matrix)
