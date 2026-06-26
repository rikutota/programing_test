#DFSバージョン

import sys
from collections import deque

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())

grid = [input().strip() for _ in range(H)]
visited = [[False]*W for _ in range(H)]

ans = 0

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(y, x):
    visited[y][x] = True

    for dy,dx in directions:
        ny = y + dy
        nx = x + dx

        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if grid[ny][nx] == ".":
            continue
        if visited[ny][nx]:
            continue

        dfs(ny, nx)

for sy in range(H):
    for sx in range(W):
        if grid[sy][sx] == ".":
            continue
        if visited[sy][sx]:
            continue

        q = deque()
        q.append((sy,sx))
        visited[sy][sx] = True

        ans += 1
        dfs(sy,sx)

print(ans)