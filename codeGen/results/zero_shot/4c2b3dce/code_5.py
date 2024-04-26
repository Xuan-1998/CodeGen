def contains_AB_and_BA(s):
    # Find all occurrences of "AB" and "BA"
    ab_positions = []
    ba_positions = []
    
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB":
            ab_positions.append(i)
        elif s[i:i+2] == "BA":
            ba_positions.append(i)
    
    # Check for non-overlapping "AB" and "BA"
    for ab_pos in ab_positions:
        for ba_pos in ba_positions:
            if abs(ab_pos - ba_pos) > 1:  # Ensure non-overlapping
                return "YES"
    
    return "NO"

# Read input from stdin
s = input().strip()
print(contains_AB_and_BA(s))
