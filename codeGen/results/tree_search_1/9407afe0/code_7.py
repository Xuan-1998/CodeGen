import sys

def is_possible_set_score(a, b, final_set=False):
    if final_set:
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def find_best_match_score(a, b):
    # Initialize the possible outcomes matrix
    possible_outcomes = [[[] for _ in range(4)] for _ in range(4)]
    
    # Fill in the base cases (either team wins 3 sets)
    for i in range(4):
        if is_possible_set_score(a, b, final_set=(i == 2)):
            possible_outcomes[3][i].append((a, b))
        if is_possible_set_score(b, a, final_set=(i == 2)):
            possible_outcomes[i][3].append((b, a))

    # Trace back from the winning scenarios
    for total_sets in range(2, 5):
        for a_wins in range(max(0, total_sets - 3), min(3, total_sets) + 1):
            b_wins = total_sets - a_wins
            if a_wins < 3 and b_wins < 3:
                continue
            for a_score, b_score in possible_outcomes[a_wins][b_wins]:
                # Check previous sets
                for prev_a in range(a_score + 2):
                    for prev_b in range(b_score + 2):
                        if is_possible_set_score(prev_a, prev_b, final_set=(total_sets == 4)):
                            if a_wins > b_wins:
                                possible_outcomes[a_wins-1][b_wins].append((prev_a, prev_b))
                            else:
                                possible_outcomes[a_wins][b_wins-1].append((prev_a, prev_b))

    # Find the best match score
    for a_wins in range(3, -1, -1):
        for b_wins in range(3, -1, -1):
            if possible_outcomes[a_wins][b_wins]:
                return f"{a_wins}:{b_wins} " + " ".join(map(str, possible_outcomes[a_wins][b_wins][0]))
    return "Impossible"

# Read input from stdin
m = int(sys.stdin.readline().strip())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(find_best_match_score(a, b))
