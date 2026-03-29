import sys

k = int(input())  # get the maximum jump distance k
stones = list(map(int, input().split()))  # get the positions of stones in ascending order

dp = {(0, d): True for d in range(k+1)}  # base case: frog can always reach stone 0 with any number of jumps <= k
for i in range(1, len(stones)):
    dp[(i, 0)] = False  # frog cannot jump from one stone to another without making a jump
    for d in range(min(k+1, i)+1):
        if any(dp.get((j, d-k-1)) or dp.get((j, d-k)) or dp.get((j, d-k+1)) for j in range(i) if stones[j] <= i - k):
            dp[(i, d)] = True
        else:
            dp[(i, d)] = False

print(any(dp.get((len(stones)-1, d)) for d in range(k+1)))  # check if the frog can reach the last stone with any number of jumps <= k
