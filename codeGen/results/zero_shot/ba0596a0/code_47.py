import sys

stones = list(map(int, input().split()))
k = abs(stones[0] - stones[1])

for i in range(2, len(stones)):
    if abs(stones[i-1] - stones[i]) != k and abs(stones[i-1] - stones[i]) not in [k - 1, k + 1]:
        print("False")
        sys.exit()

print("True")
