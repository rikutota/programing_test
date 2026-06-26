import sys

input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

INF = 10**30

dp = [INF] * N

dp[0] = 0

for i in range(1, N):
    cost_from_prev = dp[i - 1] + abs(H[i] - H[i-1])

    dp[i] = min(dp[i], cost_from_prev)

    if i >= 2:
        cost_from_prev2 = dp[i-2] + abs(H[i] - H[i-2])

        dp[i] = min(dp[i], cost_from_prev2)

print(dp[N-1])