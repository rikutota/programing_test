import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)

current = 0
cnt[0] = 1

ans = 0

for x in A:
    current += x

    ans += cnt[current - K]

    cnt[current] += 1

print(ans)