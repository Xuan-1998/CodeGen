import sys

# Read input
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate total available players
total_available_players = sum(s) - s[h-1]

code_block_start
