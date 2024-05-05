import sys

def solve():
    n = int(sys.stdin.readline())
    moods = list(map(int, sys.stdin.readline().split()))
    
    good_mood_count = 0
    for mood in moods:
        if mood == 1:
            good_mood_count += 1
    
    if good_mood_count % (n // 2) == 0 and n >= 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
