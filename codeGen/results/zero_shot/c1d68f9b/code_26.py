import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

good_mood_knights = sum(moods)
sides = len(str(n))

if good_mood_knights == 0:
    print("NO")
elif n % good_mood_knights != 0 or sides < good_mood_knights:
    print("NO")
else:
    print("YES")
