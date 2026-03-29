n = int(input())
moods = list(map(int, input().split()))
total_good = sum(moods)

if total_good > 0 and n >= 3:
    if total_good % n == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
