from dsu import DSU


class MST:

    def __init__(self, graph, nodes):
        self.edges = []
        self.n = len(graph)

        for row in range(self.n):
            if nodes[row]:
                for col in range(self.n):
                    if nodes[col]:
                        self.edges.append((graph[row][col], (row, col)))

        self.edges.sort()

    def getMST(self):

        mst = []
        dsu = DSU()
        for edge in self.edges:
            n1 = edge[1][0]
            n2 = edge[1][1]
            if dsu.isConnected(n1, n2):
                continue
            dsu.union(n1, n2)
            mst.append(edge)
        return mst

