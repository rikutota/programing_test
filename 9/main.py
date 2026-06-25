import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = []

for _ in range(Q):
    X = int(input())

    count = bisect.bisect_right(A,X)
    ans.append(str(count))

print("\n".join(ans))