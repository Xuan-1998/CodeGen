import math

n = int(input())
moods = list(map(int, input().split()))

good_moods = sum(mood for mood in moods if mood == 1)
avg = good_moods / n

if math.isclose(avg, round(avg)):
    print("YES")
else:
    print("NO")
