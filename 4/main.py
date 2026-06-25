import sys
from collections import Counter

def solve():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    cnt = Counter(A)
    ans = max(cnt.values())

    print(ans)

if __name__ == "__main__":
    solve()