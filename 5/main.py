import sys
from collections import Counter

def solve():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    cnt = Counter(A)

    ans = 0

    # nC2を解く
    for c in cnt.values():
        ans += c * (c - 1) // 2

    print(ans)

if __name__ == "__main__":
    solve()