n = int(input())
moods = list(map(int, input().split()))
in_good_mood = all((mood == (i % 2)) for i, mood in enumerate(moods))
can_form_polygon = in_good_mood and n > 2
print("YES" if can_form_polygon else "NO")
