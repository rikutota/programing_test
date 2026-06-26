import sys

input = sys.stdin.readline

# N: 数の個数
# K: 作りたい合計
N, K = map(int, input().split())
# A: 選ぶ候補となる整数列
A = list(map(int, input().split()))

dp = [False] * (K+1)

dp[0] = True

for x in A:
    for s in range(K, x - 1, -1):
        if dp[s-x]:
            dp[s] = True

print(dp[K])