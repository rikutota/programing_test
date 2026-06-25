import sys

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 10**18

for i in range(N-1):
    diff = A[i+1]-A[i]

    ans = min(ans, diff)

print(ans)