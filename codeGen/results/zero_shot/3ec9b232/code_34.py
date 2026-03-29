from sys import stdin, stdout
n = int(stdin.readline())
m = list(map(int, stdin.readline().split()))
# Step 1: Count the frequency of each number in M
freq = {}
for x in m:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Step 2: Calculate the number of ways to create V
ways = 1
for k, v in freq.items():
    ways *= (v + 1)
ways %= 10**9 + 7

print(ways)
