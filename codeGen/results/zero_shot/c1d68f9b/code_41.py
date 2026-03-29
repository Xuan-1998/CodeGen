def can_form_regular_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    # Calculate the total mood
    total_mood = sum(moods)
    
    # Check if all moods are equal
    for mood in set(moods):
        if mood != 0 and (total_mood // n) * n + n != total_mood:
            return "NO"
    
    return "YES"

print(can_form_regular_polygon())
