import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
each_friends_list = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    each_friends_list[a].append(b)
    each_friends_list[b].append(a)

visited = [False] * (N+1)

ans = 0

for start in range(N):
    if visited[start]:
        continue
    ans += 1

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        for nv in each_friends_list[v]:
            if visited[nv]:
                continue

            visited[nv] = True
            q.append(nv)

print(ans)