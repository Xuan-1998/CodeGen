import sys

n = int(sys.stdin.readline())
monster_appearances = list(map(int, sys.stdin.readline().split()))
monster_healths = list(map(int, sys.stdin.readline().split()))

# Sort monster appearances in ascending order
monster_appearances.sort()
