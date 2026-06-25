import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))

hq = []

for x in A:
    if len(hq) < K:
        heapq.heappush(hq, x)
    else:
        heapq.replace(hq, x)

print(sum(hq))