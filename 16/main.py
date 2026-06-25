from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

grid = [input().strip() for _ in range(H)]

dist = [[-1]*W for _ in range(H)]

q = deque()

dist[sy][sx] = 0
q.append((sy, sx))

directions =[(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y,x = q.popleft()

    for dy, dx in directions:
        ny = y+dy
        nx = x+dx

        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if dist[ny][nx] != -1:
            continue

        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))

print(dist[gy][gx])


