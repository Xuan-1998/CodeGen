import sys

def is_valid_set_score(a, b, final_set=False):
    if final_set:  # For the final set, the minimum winning score is 15
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:  # For the first four sets, the minimum winning score is 25
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def find_best_match_score(scores):
    sets_won_by_a = sets_won_by_opponent = 0
    set_results = []

    for i, (a, b) in enumerate(scores):
        # Check if the set score is valid
        if not is_valid_set_score(a, b, final_set=(i == 4)):
            return "Impossible"
        # Update the number of sets won by each team
        if a > b:
            sets_won_by_a += 1
        else:
            sets_won_by_opponent += 1
        # Add the set result
        set_results.append(f"{a}:{b}")
        # Check if the match can be concluded
        if sets_won_by_a == 3 or sets_won_by_opponent == 3:
            break

    # Construct the match score
    match_score = f"{sets_won_by_a}:{sets_won_by_opponent}"
    return match_score + " " + " ".join(set_results)

# Read the number of matches
m = int(sys.stdin.readline().strip())
for _ in range(m):
    scores = []
    for _ in range(5):  # Read the scores for up to five sets
        a, b = map(int, sys.stdin.readline().strip().split())
        scores.append((a, b))
    print(find_best_match_score(scores))
