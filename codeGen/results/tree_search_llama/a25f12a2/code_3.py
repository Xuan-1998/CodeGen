import sys

heads, tails = map(int, sys.stdin.readline().split())

orthus_count = heads // 2
hydra_count = tails // 3

if orthus_count * hydra_count == heads and orthus_count * hydra_count == tails:
    print([orthus_count, hydra_count])
else:
    print("No solutions")
