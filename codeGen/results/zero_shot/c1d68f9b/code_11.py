import sys

def can_form_regular_polygon():
    n = int(sys.stdin.readline())
    moods = list(map(int, sys.stdin.readline().split()))
    
    good_moods = sum(mood for mood in moods if mood == 1)
    
    if good_moods % n == 0:
        print("YES")
    else:
        print("NO")

can_form_regular_polygon()
