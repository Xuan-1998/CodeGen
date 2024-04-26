import sys

def volleyball_match(a, b):
    # Constants for the minimum winning scores
    MIN_WIN_SCORE = 25
    FINAL_SET_SCORE = 15
    
    # Function to check if a set score is valid
    def is_valid_set(score_a, score_b, final_set=False):
        if final_set:
            min_win_score = FINAL_SET_SCORE
        else:
            min_win_score = MIN_WIN_SCORE
        return (score_a >= min_win_score or score_b >= min_win_score) and abs(score_a - score_b) >= 2
    
    # Function to calculate the possible set outcomes
    def calculate_sets(a, b):
        sets = []
        for i in range(3):
            for j in range(3):
                if i + j >= 3:
                    continue
                for final_set in [False, True]:
                    score_a = [0] * i + [MIN_WIN_SCORE - 1] * (2 - i)
                    score_b = [0] * j + [MIN_WIN_SCORE - 1] * (2 - j)
                    while sum(score_a) < a and sum(score_b) < b:
                        if final_set and sum(score_a) + sum(score_b) == a + b - FINAL_SET_SCORE:
                            score_a.append(FINAL_SET_SCORE - 1)
                            score_b.append(FINAL_SET_SCORE - 1)
                            break
                        score_a.append(MIN_WIN_SCORE)
                        score_b.append(MIN_WIN_SCORE)
                    if is_valid_set(score_a[-1], score_b[-1], final_set):
                        sets.append((i + j, score_a, score_b))
        return sets

    # Calculate possible set outcomes
    possible_sets = calculate_sets(a, b)
    
    # Find the best match score
    for sets_won, score_a, score_b in possible_sets:
        if all(is_valid_set(score_a[i], score_b[i], i == len(score_a) - 1) for i in range(len(score_a))):
            return f"{3 - sets_won}:{sets_won} " + " ".join(f"{x}:{y}" for x, y in zip(score_a, score_b))
    
    return "Impossible"

# Read the number of matches
m = int(sys.stdin.readline().strip())

# Process each match
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(volleyball_match(a, b))
