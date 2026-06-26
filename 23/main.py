import sys

input = sys.stdin.readline

N, W = map(int, input().split())

dp = [0]*(W+1)

for _ in range(N):
    w,v = map(int, input().split())

    for weight in range(W, w - 1, -1):
        not_choose = dp[weight]
        choose = dp[weight] + v
        dp[weight] = map(not_choose, choose)

print(dp[W])