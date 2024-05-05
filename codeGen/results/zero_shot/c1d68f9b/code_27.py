def can_form_polygon(moods):
    return all(mood == 1 for mood in moods)

n = int(input())
moods = list(map(int, input().split()))

print("YES" if can_form_polygon(moods) else "NO")
