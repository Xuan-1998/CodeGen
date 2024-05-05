import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))
good_mood_count = 0

for i in range(n):
    if moods[i] == 1:
        good_mood_count += 1
    else:
        good_mood_count -= 1

print("YES" if good_mood_count % 2 != 0 and n > 2 else "NO")
