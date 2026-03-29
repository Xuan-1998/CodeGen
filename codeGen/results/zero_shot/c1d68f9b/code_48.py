n = int(input())
moods = list(map(int, input().split()))
if all(mood == 1 for mood in moods):
    if n % 2:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
