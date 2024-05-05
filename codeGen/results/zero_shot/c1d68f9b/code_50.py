import sys

def main():
    n = int(sys.stdin.readline())
    moods = list(map(int, sys.stdin.readline().split()))
    
    good_mood_count = sum(moods)
    
    if 0 in moods:
        return "NO"
    elif good_mood_count == n or good_mood_count == 0:
        return "YES"
    else:
        # Check for odd/even number of good knights
        even_good_knights = sum(1 for mood in moods if mood)
        if n % 2 == 1 and even_good_knights > 0:
            return "NO"
        elif n % 2 == 0 and (even_good_knights != 0 or good_mood_count != 0):
            return "NO"
        else:
            return "YES"

print(main())
