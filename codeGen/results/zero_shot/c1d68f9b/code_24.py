import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))
good_knights = [i for i in range(n) if moods[i] == 1]

if len(good_knights) < 3:
    print("NO")
else:
    prev_good = good_knights[0]
    for knight in good_knights[1:]:
        if abs(knight - prev_good) != 1:
            print("NO")
            break
    else:
        print("YES")
