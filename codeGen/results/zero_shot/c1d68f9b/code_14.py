import sys

def can_form_polygon(moods):
    n = int(sys.stdin.readline())
    knights_in_good_mood = sum(map(int, sys.stdin.readline().split()))
    
    if n < 3 or (n % 2 == 1 and knights_in_good_mood > 0) or (n % 2 == 0 and knights_in_good_mood != n):
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    print(can_form_polygon([0, 0, 1]))
