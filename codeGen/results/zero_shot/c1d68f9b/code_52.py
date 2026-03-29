import sys

n = int(input())
moods = list(map(int, input().split()))

good_mood_knights = 0
for mood in moods:
    if mood == 1:
        good_mood_knights += 1

if n % (2*good_mood_knights) == 0 and good_mood_knights > 2:
    print("YES")
else:
    print("NO")
