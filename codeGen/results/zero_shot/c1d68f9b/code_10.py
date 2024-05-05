n = int(input())
moods = list(map(int, input().split()))
total_good_moods = sum(mood for mood in moods if mood == 1)
print("YES" if total_good_moods >= 3 and (total_good_moods % 3) == 0 else "NO")
