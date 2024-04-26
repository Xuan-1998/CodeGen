def is_set_won(a, b, is_final_set=False):
    min_points = 15 if is_final_set else 25
    return (a >= min_points and a - b >= 2) or (b >= min_points and b - a >= 2)

def get_match_score(sets):
    a_wins = b_wins = 0
    for i, (a, b) in enumerate(sets):
        if is_set_won(a, b, i == 4):
            if a > b:
                a_wins += 1
            else:
                b_wins += 1
        else:
            return "Impossible"
    if a_wins == 3 or b_wins == 3:
        return f"{a_wins}:{b_wins}"
    return "Impossible"

def main():
    m = int(input().strip())
    for _ in range(m):
        sets = []
        for _ in range(5):
            a, b = map(int, input().split())
            sets.append((a, b))
        print(get_match_score(sets))

if __name__ == "__main__":
    main()
