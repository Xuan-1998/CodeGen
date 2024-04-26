def is_possible_set(score_a, score_b, is_final_set=False):
    min_points = 15 if is_final_set else 25
    if score_a < min_points and score_b < min_points:
        return False
    if abs(score_a - score_b) < 2:
        return False
    return (score_a > score_b and score_a >= min_points) or (score_b > score_a and score_b >= min_points)

def calculate_sets(a, b):
    sets = []
    for i in range(4):
        for score_a in range(25, a + 1):
            score_b = a + b - score_a
            if is_possible_set(score_a, score_b):
                sets.append((score_a, score_b))
                a -= score_a
                b -= score_b
                break
        else:  # No break, impossible to find a valid score for this set
            return "Impossible"
    # Check the fifth set if necessary
    if a > 0 or b > 0:
        if not is_possible_set(a, b, is_final_set=True):
            return "Impossible"
        sets.append((a, b))
    # Count wins
    wins_a = sum(1 for score_a, score_b in sets if score_a > score_b)
    wins_b = len(sets) - wins_a
    if wins_a < 3 and wins_b < 3:
        return "Impossible"
    return f"{wins_a}:{wins_b} " + " ".join(f"{score_a}:{score_b}" for score_a, score_b in sets)

def main():
    m = int(input().strip())
    for _ in range(m):
        a, b = map(int, input().strip().split())
        result = calculate_sets(a, b)
        print(result)

if __name__ == "__main__":
    main()
