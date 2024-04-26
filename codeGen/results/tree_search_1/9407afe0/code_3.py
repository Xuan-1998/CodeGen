import sys

def find_match_score(a, b, set_scores, a_sets_won, b_sets_won, set_number):
    # Base case: if either team has won 3 sets, the match is over
    if a_sets_won == 3 or b_sets_won == 3:
        if a == 0 and b == 0:  # Check if all points have been accounted for
            return f"{a_sets_won}:{b_sets_won} " + " ".join(map(str, set_scores))
        else:
            return "Impossible"

    # Set the minimum winning score depending on the set number
    min_win_score = 15 if set_number == 4 else 25

    # Try all possible scores for the current set
    for a_score in range(min_win_score, a + 1):
        for b_score in range(min_win_score, b + 1):
            if abs(a_score - b_score) >= 2:  # A team must win by at least 2 points
                if a_score > b_score:  # Team A wins the set
                    result = find_match_score(a - a_score, b - b_score, set_scores + [f"{a_score}:{b_score}"], a_sets_won + 1, b_sets_won, set_number + 1)
                else:  # Opponent wins the set
                    result = find_match_score(a - a_score, b - b_score, set_scores + [f"{a_score}:{b_score}"], a_sets_won, b_sets_won + 1, set_number + 1)
                if result != "Impossible":
                    return result

    return "Impossible"

# Read the number of matches from stdin
m = int(sys.stdin.readline().strip())

# Process each match
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(find_match_score(a, b, [], 0, 0, 0))
