import sys
import heapq

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

heapq.heapify(A)

ans = 0

while len(A) > 1:
    x = heapq.heappop(A)
    y = heapq.heappop(A)

    cost = x + y
    ans += cost

    heapq.heappush(A, cost)

print(ans)