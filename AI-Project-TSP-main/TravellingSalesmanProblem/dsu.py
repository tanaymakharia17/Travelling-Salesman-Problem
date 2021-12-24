class DSU:

    def __init__(self):
        self.par = {}
        self.rnk = {}

    def find(self, x):

        if self.par.get(x, x) != x:
            self.par[x] = self.find(self.par[x])

        return self.par.get(x, x)

    def isConnected(self, x, y):

        return self.find(x) == self.find(y)

    def union(self, x, y):

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.rnk.get(x, 0) > self.rnk.get(y, 0):
            self.par[y] = x
            self.rnk[x] = self.rnk.get(x, 0) + 1
        else:
            self.par[x] = y
            self.rnk[y] = self.rnk.get(y, 0) + 1

