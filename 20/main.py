import sys

input = sys.stdin.readline
N = int(input())

MOD = 10**9 + 7

dp = [0] * (N + 1)

dp[0] = 1

for i in range(1, N+1):
    dp[i] += dp[i-1]

    if i >= 2:
        dp[i] += dp[i-2]

    dp[i] %= MOD

print(dp[N])