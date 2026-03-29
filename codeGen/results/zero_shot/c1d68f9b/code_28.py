code
n = int(input())
moods = list(map(int, input().split()))

if n % 2 != 0:
    print("NO")
else:
    for mood in moods:
        if mood != 1:
            print("NO")
            break
    else:
        print("YES")
