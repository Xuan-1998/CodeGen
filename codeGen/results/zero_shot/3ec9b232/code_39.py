# Input
n = int(input())
M = list(map(int, input().split()))

# Initialize count of arrays that can be merged into M
count = 0

# Iterate over all possible arrays V
for V in itertools.product(range(1, n+1), repeat=n):
    # Check if merging V into a sorted array results in M
    if sorted(V) == M:
        count += 1

print(count % (10**9 + 7))
