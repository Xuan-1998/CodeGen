def is_possible_set_score(a, b, final_set=False):
    if final_set:
        # In the final set, a team must score at least 15 points to win and must win by 2 points.
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:
        # In the first four sets, a team must score at least 25 points to win and must win by 2 points.
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def determine_sets(a, b):
    sets_a, sets_b = 0, 0
    set_scores = []
    while a > 0 and b > 0:
        if sets_a == 2 and sets_b == 2:
            # Final set rules.
            if is_possible_set_score(a, b, final_set=True):
                sets_a += a > b
                sets_b += b > a
                set_scores.append((a, b))
                a = b = 0
            else:
                return "Impossible", []
        else:
            # Regular set rules.
            if is_possible_set_score(a, b):
                sets_a += a > b
                sets_b += b > a
                set_scores.append((a, b))
                a -= 25 if a > b else 0
                b -= 25 if b > a else 0
            else:
                return "Impossible", []
        if sets_a == 3 or sets_b == 3:
            break
    if sets_a == 3 or sets_b == 3:
        return f"{sets_a}:{sets_b}", set_scores
    else:
        return "Impossible", []

def process_matches(m, matches):
    for a, b in matches:
        match_score, set_scores = determine_sets(a, b)
        if match_score == "Impossible":
            print(match_score)
        else:
            formatted_set_scores = ' '.join(f"({x},{y})" for x, y in set_scores)
            print(f"{match_score} {formatted_set_scores}")

def main():
    m = int(input().strip())
    matches = [tuple(map(int, input().strip().split())) for _ in range(m)]
    process_matches(m, matches)

if __name__ == "__main__":
    main()
