def is_valid_set_score(a, b, final_set=False):
    if final_set:  # For the final (5th) set
        return (a >= 15 or b >= 15) and abs(a - b) == 2
    else:  # For the first four sets
        return (a >= 25 or b >= 25) and abs(a - b) == 2

def find_best_match_score(a, b):
    # We will simulate all possible combinations of set outcomes
    for a_wins in range(4):
        for b_wins in range(4):
            # The total number of sets played cannot exceed 5
            if a_wins + b_wins > 4:
                continue
            # Determine the number of points needed to win the remaining sets
            a_needed = 25 * a_wins + (15 if a_wins == 3 else 0)
            b_needed = 25 * b_wins + (15 if b_wins == 3 else 0)
            # Check if it's possible to reach the given scores
            if a >= a_needed and b >= b_needed and (a - a_needed) % 2 == 0 and (b - b_needed) % 2 == 0:
                # Check if the last set scores are valid
                final_set = a_wins == 3 or b_wins == 3
                if is_valid_set_score(a - a_needed, b - b_needed, final_set):
                    # If all conditions are met, return the match score
                    return f"{a_wins}:{b_wins} ({a - a_needed}:{b - b_needed})"
    # If no valid match score is found, return "Impossible"
    return "Impossible"

# Read the number of matches from stdin
m = int(input().strip())
for _ in range(m):
    a, b = map(int, input().split())
    print(find_best_match_score(a, b))
