import sys

input = sys.stdin.readline

N = int(input())

jobs = []

for _ in range(N):
    A, B = map(int, input().split())
    jobs.append(B,A)

jobs.sort()

current_time = 0

for deadline, duration in jobs:
    current_time = duration

    if current_time > deadline:
        print("No")
        exit()

print("Yes")