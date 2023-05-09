class disjointSet :
    def __init__(self, n) -> None:
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.n = n
    
    def find(self, x) :
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
     
    def union(self, x, y) :
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot :
            return
        if self.rank[xRoot] < self.rank[yRoot] :
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot] :
            self.parent[yRoot] = xRoot
        else :
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += 1
            
ds = disjointSet(11)
ds.union(0, 1)
ds.union(2, 3)
ds.union(3, 4)
ds.union(7, 10)
print(ds.rank)