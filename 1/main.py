from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
ans = 0

for a in A:
    need = K - a

    ans += cnt[need]
    cnt[a] += 1

print(ans)