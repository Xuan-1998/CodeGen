stones = [int(x) for x in input().split()]
if stones[1] <= 2:  # or stones[1] - stones[0] in [1, 2]:
    print("Yes")
else:
    print("No")

for i in range(1, len(stones) - 1):
    if abs(stones[i] - stones[i-1]) not in [1, 2]:
        print("No")
print("Yes")
