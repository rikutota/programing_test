import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

for bit in range(1 << N):
    sum = 0

    for i in range(N):
        if bit & (1 << i):
            sum += A[i]

    if sum == K:
        print("Yes")
        exit()

print("No")

