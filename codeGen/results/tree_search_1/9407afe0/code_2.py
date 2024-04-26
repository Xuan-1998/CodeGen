import sys

def is_possible_set_score(a, b, is_final_set=False):
    min_points = 15 if is_final_set else 25
    return (a >= min_points or b >= min_points) and abs(a - b) >= 2

def find_best_match_score(a, b):
    # Early check for an impossible score
    if a < 0 or b < 0 or (a == 0 and b == 0):
        return "Impossible"
    
    # Try all combinations of set wins for Team A and their opponent
    for sets_won_by_A in range(4):
        for sets_won_by_opponent in range(4):
            if sets_won_by_A == 3 or sets_won_by_opponent == 3:
                set_scores = []
                remaining_a, remaining_b = a, b
                for set_number in range(1, 6):
                    for score_a in range(0, remaining_a + 1):
                        score_b = remaining_b - (remaining_a - score_a)
                        is_final_set = set_number == 5
                        if is_possible_set_score(score_a, score_b, is_final_set):
                            set_scores.append((score_a, score_b))
                            remaining_a -= score_a
                            remaining_b -= score_b
                            break
                    if len(set_scores) < set_number:
                        break
                if len(set_scores) == sets_won_by_A + sets_won_by_opponent:
                    A_wins = sum(1 for score_a, score_b in set_scores if score_a > score_b)
                    opponent_wins = sum(1 for score_a, score_b in set_scores if score_a < score_b)
                    if A_wins == sets_won_by_A and opponent_wins == sets_won_by_opponent:
                        return "{}:{} {}".format(A_wins, opponent_wins, ' '.join("{}:{}".format(sa, sb) for sa, sb in set_scores))
    
    return "Impossible"

# Read input from stdin
m = int(input().strip())
for _ in range(m):
    a, b = map(int, input().strip().split())
    print(find_best_match_score(a, b))
