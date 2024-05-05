n = int(input())
moods = list(map(int, input().split()))
if all(mood == 1 for mood in moods):
    print("YES")
else:
    print("NO")
