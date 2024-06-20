V, E = map(int, input().split())

edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

UnionSet = [i for i in range(V + 1)]

def find(x):
    curr = x
    path = []
    while UnionSet[curr] != curr:
        path.append(curr)
        curr = UnionSet[curr]
    for node in path:
        UnionSet[node] = curr
    return curr

def union(x, y):
    x = find(x)
    y = find(y)
    UnionSet[y] = x

sumOfEdges = 0

for edge in edges:
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        sumOfEdges += edge[0]

print(sumOfEdges)