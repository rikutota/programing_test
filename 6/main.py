import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    ans = 0

    for x in A:
        need = K - x

        # 今までに need が出ていた回数だけ、今の x とペアが作れる
        ans += cnt[need]

        # 今の x を「これまでに出た値」として記録する
        cnt[x] += 1

    print(ans)

if __name__ == "__main__":
    solve()