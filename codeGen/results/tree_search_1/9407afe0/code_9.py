import sys

def is_valid_set(a, b, is_final_set):
    if is_final_set:
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def find_possible_scores(a, b, set_scores, current_score, sets_needed, is_final_set):
    if sets_needed == 0:
        if sum(x[0] for x in set_scores) == a and sum(x[1] for x in set_scores) == b:
            return current_score + ":" + str(3 - int(current_score)) + " " + " ".join(f"{x[0]}:{x[1]}" for x in set_scores)
        else:
            return None

    for i in range(a+1):
        for j in range(b+1):
            if is_valid_set(i, j, is_final_set):
                if i > j:
                    result = find_possible_scores(a-i, b-j, set_scores+[(i, j)], current_score, sets_needed-1, sets_needed == 1)
                else:
                    result = find_possible_scores(a-i, b-j, set_scores+[(i, j)], str(int(current_score)-1), sets_needed-1, sets_needed == 1)
                if result:
                    return result
    return None

def volleyball_match_score(a, b):
    for sets_won in range(3, -1, -1):
        result = find_possible_scores(a, b, [], str(sets_won), 3, False)
        if result:
            return result
    return "Impossible"

# Read number of matches
m = int(sys.stdin.readline().strip())

# Process each match
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(volleyball_match_score(a, b))
