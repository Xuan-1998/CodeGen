def can_form_polygon():
    n = int(input())  # Read number of knights
    moods = list(map(int, input().split()))  # Read moods of knights
    
    good_mood_count = sum(moods)  # Count the number of knights in a good mood
    if good_mood_count % (n // 2) != 0:  # Check if the count is divisible by half the number of knights
        return "NO"  # If not, it's impossible to form a polygon
    else:
        return "YES"  # If yes, it's possible to form a polygon
    
print(can_form_polygon())
