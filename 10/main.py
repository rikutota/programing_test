import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def ok(T):
    total = 0
    for a in A:
        total += T // a
        if total >= K:
            return True
        return False

ng = 0
ok_time = min(A) * K

while ok_time -ng > 1:
    mid = (ok_time + ng) // 2

    if ok(mid):
        ok_time = mid
    else:
        ng = mid

print(ok_time)