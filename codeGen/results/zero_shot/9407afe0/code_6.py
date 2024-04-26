def is_valid_set_score(a, b, final_set=False):
    # For final set, the minimum score is 15, otherwise it's 25
    min_score = 15 if final_set else 25
    if a < min_score and b < min_score:
        return False
    if abs(a - b) < 2:
        return False
    if (a >= min_score or b >= min_score) and (a >= b + 2 or b >= a + 2):
        return True
    return False

def find_best_match_score(a, b):
    sets = []
    a_wins = b_wins = 0

    # Check each set for a valid score
    for i in range(4):
        if is_valid_set_score(a[i], b[i]):
            if a[i] > b[i]:
                a_wins += 1
            else:
                b_wins += 1
            sets.append((a[i], b[i]))
        else:
            return "Impossible"
        if a_wins == 3 or b_wins == 3:
            break

    # Check the final set if necessary
    if a_wins < 3 and b_wins < 3:
        if not is_valid_set_score(a[4], b[4], final_set=True):
            return "Impossible"
        if a[4] > b[4]:
            a_wins += 1
        else:
            b_wins += 1
        sets.append((a[4], b[4]))

    return f"{a_wins}:{b_wins} " + " ".join(f"{a}:{b}" for a, b in sets)

def main():
    m = int(input().strip())
    for _ in range(m):
        points = list(map(int, input().strip().split()))
        a_points = points[::2]
        b_points = points[1::2]
        result = find_best_match_score(a_points, b_points)
        print(result)

if __name__ == "__main__":
    main()
