import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

ans = []

for _ in range(Q):
    L,R = map(int, input().split())
    ans.append(str(S[R]-S[L-1]))

for a in ans:
    print(a)