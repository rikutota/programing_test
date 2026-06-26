import sys

input = sys.stdin.readline

# N: 配列Aの長さ
N = int(input())
# A: 選ぶ候補となる整数列
A = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    not_choose = dp[i-1]

    choose = dp[i-1]

    if i >= 2:
        choose += dp[i-2]

    dp[i] = max(not_choose, choose)

print(dp(N))