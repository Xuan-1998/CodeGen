import sys

stones = [int(x) for x in input().split()]
k = int(input())

for i in range(1, len(stones)):
    if not can_reach_next(stones[i-1], k):
        print("False")
        break
else:
    print("True")

