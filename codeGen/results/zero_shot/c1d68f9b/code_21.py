import sys

def is_polygon_formable(knights_moods):
    # Check if there are at least 3 knights
    if len(knights_moods) < 3:
        return "NO"
    
    # Calculate the sum of moods
    total_mood = sum(knights_moods)
    
    # If the sum is not equal to 0 or n, a polygon cannot be formed
    if total_mood != 0 and total_mood != len(knights_moods):
        return "NO"
    
    return "YES"


# Read input from standard input
n = int(sys.stdin.readline())
knights_moods = list(map(int, sys.stdin.readline().split()))

print(is_polygon_formable(knights_moods))
