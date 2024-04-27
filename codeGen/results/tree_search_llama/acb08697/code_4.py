import sys

n = int(sys.stdin.readline())
operations = list(sys.stdin.readline().strip())

# Count additions (+) and removals (-)
additions = operations.count('+')
removals = operations.count('-')

# The minimum possible number of stones is when additions equal removals
min_stones = abs(additions - removals)

print(min_stones)
