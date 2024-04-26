def is_possible_set(score_a, score_b, is_final_set=False):
    # Check if the score is possible for a set
    min_score = 15 if is_final_set else 25
    if score_a >= min_score or score_b >= min_score:
        if abs(score_a - score_b) >= 2 or (is_final_set and (score_a == 15 or score_b == 15)):
            return True
    return False

def find_best_match_score(a, b):
    # Initialize set wins for both teams
    sets_won_a = sets_won_b = 0
    set_scores = []
    
    # Simulate sets based on the scores
    while a > 0 and b > 0 and (sets_won_a < 3 and sets_won_b < 3):
        if sets_won_a == 2 and sets_won_b == 2:
            # Final set
            if is_possible_set(a, b, True):
                sets_won_a += a > b
                sets_won_b += b > a
                set_scores.append(f"{a}-{b}")
                break
            else:
                return "Impossible"
        else:
            # Regular set
            if is_possible_set(a, b):
                sets_won_a += a > b
                sets_won_b += b > a
                set_scores.append(f"{a}-{b}")
                a -= 25 if a > b else 0
                b -= 25 if b > a else 0
            else:
                return "Impossible"
    
    # If one of the teams won 3 sets, format the output
    if sets_won_a == 3 or sets_won_b == 3:
        return f"{sets_won_a}:{sets_won_b} {' '.join(set_scores)}"
    else:
        return "Impossible"

# Read the number of matches
m = int(input().strip())

# Process each match
for _ in range(m):
    a, b = map(int, input().strip().split())
    print(find_best_match_score(a, b))
