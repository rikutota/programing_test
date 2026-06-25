import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        if abs(A[j] - A[i]) <= K:
            cnt += 1

print(cnt)