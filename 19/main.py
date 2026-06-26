import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    A,B = map(int, input().split())
    A -= 1
    B -= 1

    graph[A].append(B)
    graph[B].append(A)

    depth = [-1] * N

    root = 0
    depth[root] = 0

    stack = [root]

    while stack:
        v = stack.pop()

        for nv in graph[v]:
            if depth[nv] != -1:
                continue

            depth[nv] = depth[v] + 1

            stack.append(nv)
print(*depth)