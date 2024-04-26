import sys

def is_valid_set_score(a, b, final_set=False):
    if final_set:
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def reconstruct_match(a, b):
    set_scores = []
    sets_a, sets_b = 0, 0
    
    for _ in range(4):  # First 4 sets
        for score_a in range(25, a+1):
            score_b = a + b - score_a
            if is_valid_set_score(score_a, score_b):
                set_scores.append((score_a, score_b))
                if score_a > score_b:
                    sets_a += 1
                else:
                    sets_b += 1
                a -= score_a
                b -= score_b
                break
        if sets_a == 3 or sets_b == 3:
            break
    
    if sets_a < 3 and sets_b < 3:  # Last set if needed
        if is_valid_set_score(a, b, final_set=True):
            set_scores.append((a, b))
            if a > b:
                sets_a += 1
            else:
                sets_b += 1
        else:
            return "Impossible"
    
    if sets_a == 3 or sets_b == 3:
        return f"{sets_a}:{sets_b} " + " ".join(f"{score_a}:{score_b}" for score_a, score_b in set_scores)
    else:
        return "Impossible"

# Read input from stdin
m = int(sys.stdin.readline().strip())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(reconstruct_match(a, b))
