class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.rank[root_u] += 1

            return self.size[root_u] * self.size[root_v]
        return 0

def minimum_red_edges(N, colors):
    uf = UnionFind(N)
    red_edges = 0
    
    for color in colors:
        if color == 0:
            # Find the two smallest components to connect for a red edge
            components = sorted((uf.size[i], i) for i in range(N) if uf.find(i) == i)
            if len(components) > 1:
                red_edges += uf.union(components[0][1], components[1][1])
        else:
            # Connect the largest two components for a blue edge
            components = sorted((uf.size[i], i) for i in range(N) if uf.find(i) == i)
            if len(components) > 1:
                uf.union(components[-1][1], components[-2][1])

    return red_edges

# Example usage
N = 5
colors = [1, 1, 0, 1]
print(minimum_red_edges(N, colors))
