import sys

# read input from stdin
stones = list(map(int, sys.stdin.readline().split()))

# call the function and print the result
print(can_frog_cross(stones))
