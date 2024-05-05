import sys

n = int(sys.stdin.readline().strip())
moods = list(map(int, sys.stdin.readline().strip().split()))

good_moods_count = sum(moods)

if good_moods_count >= 3:
    print("YES")
else:
    print("NO")
