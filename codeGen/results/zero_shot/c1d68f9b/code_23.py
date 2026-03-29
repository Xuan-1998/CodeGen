n = int(input())
moods = list(map(int, input().split()))
good_mood_knights = [k for k, mood in enumerate(moods) if mood == 1]

if len(good_mood_knights) < 3:
    print("NO")
else:
    print("YES")
