def is_possible_set_score(a, b, is_final_set=False):
    # In the final set, a team wins with at least 15 points and must win by 2 points.
    # In other sets, a team wins with at least 25 points and must win by 2 points.
    min_points = 15 if is_final_set else 25
    return (a >= min_points or b >= min_points) and abs(a - b) >= 2

def find_best_match_score(a, b):
    sets_a = sets_b = 0
    sets = []
    while a > 0 and b > 0:
        # Determine if it's the potential final set
        is_final_set = sets_a == 2 or sets_b == 2 or len(sets) == 4
        if not is_possible_set_score(a, b, is_final_set):
            return "Impossible"
        
        if a > b:
            sets_a += 1
            points = 15 if is_final_set else 25
            sets.append((min(a, points + (a - b - 2)), b))
            a -= sets[-1][0]
            b -= sets[-1][1]
        else:
            sets_b += 1
            points = 15 if is_final_set else 25
            sets.append((a, min(b, points + (b - a - 2))))
            a -= sets[-1][0]
            b -= sets[-1][1]
        
        if sets_a == 3 or sets_b == 3:
            break

    if sets_a < 3 and sets_b < 3:
        return "Impossible"
    
    return f"{sets_a}:{sets_b} " + " ".join(f"{set_score[0]}:{set_score[1]}" for set_score in sets)

# Read the number of matches
m = int(input())

# Process each match
for _ in range(m):
    a, b = map(int, input().split())
    print(find_best_match_score(a, b))
