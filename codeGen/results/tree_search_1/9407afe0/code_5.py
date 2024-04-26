import sys

def is_possible_set(score_a, score_b, is_final_set=False):
    if is_final_set:
        min_score, max_score = 15, 200
    else:
        min_score, max_score = 25, 200
    # Check if the score is possible for a set
    if (score_a >= min_score and score_b < score_a and score_a - score_b < 2) or (score_b >= min_score and score_a < score_b and score_b - score_a < 2):
        return False
    if score_a < min_score and score_b < min_score:
        return False
    return (score_a >= min_score and score_a - score_b >= 2) or (score_b >= min_score and score_b - score_a >= 2)

def find_best_match_score(a, b):
    # Iterate through possible set wins for 'Team A' and their opponent
    for a_wins in range(4):
        for b_wins in range(4):
            if a_wins == 3 or b_wins == 3:
                set_scores = []
                for i in range(a_wins):
                    set_scores.append((25, max(0, min(b, 23))))
                    b -= set_scores[-1][1]
                    a -= 25
                for i in range(b_wins):
                    set_scores.append((max(0, min(a, 23)), 25))
                    a -= set_scores[-1][0]
                    b -= 25
                if a_wins == 3 and b_wins < 3:
                    if is_possible_set(a, b, b_wins == 2):
                        set_scores.append((a, b))
                        return f"{a_wins}:{b_wins}", set_scores
                if b_wins == 3 and a_wins < 3:
                    if is_possible_set(a, b, a_wins == 2):
                        set_scores.append((a, b))
                        return f"{a_wins}:{b_wins}", set_scores
    return "Impossible", []

# Read input
m = int(sys.stdin.readline().strip())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    match_score, set_scores = find_best_match_score(a, b)
    if match_score == "Impossible":
        print(match_score)
    else:
        print(match_score, ' '.join(f"({x},{y})" for x, y in set_scores))

