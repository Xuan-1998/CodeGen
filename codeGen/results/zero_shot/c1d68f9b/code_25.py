import sys

def can_form_polygon(knights):
    k = sum(1 for mood in knights if mood == 1)
    if k < 3 or k > len(knights):
        return "NO"
    
    # Check if the polygon is regular
    angle = (360 / k) - 30
    for i in range(len(knights)):
        prev_mood = knights[(i-1)%len(knights)] == 1
        curr_mood = knights[i] == 1
        if abs(prev_mood - curr_mood) > angle:
            return "NO"
    
    return "YES"

# Read input from stdin
n = int(sys.stdin.readline())
knights = [int(x) for x in sys.stdin.readline().split()]

print(can_form_polygon(knights))
