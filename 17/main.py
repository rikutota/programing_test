#BFSパターン

import sys
from collections import deque

input = sys.stdin.readline

H,W = map(int, input().split())

grid = [input().strip() for _ in range(H)]

visited = [[False] * W for _ in range(H)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

ans = 0

for sy in range(H):
    for sx in range(W):
        if grid[sy][sx] == ".":
            continue
        if visited[sy][sx]:
            continue
        ans += 1

        q = deque()
        q.append((sy,sx))
        visited[sy][sx] = True

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny = y + dy
                nx = x + dx

                if not (0 <= ny <H and 0 <= nx < W):
                    continue

                if grid[ny][nx] == ".":
                    continue

                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                q.append((ny,nx))

print(ans)