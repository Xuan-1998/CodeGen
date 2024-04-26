def volleyball_match_score(a, b):
    sets = []
    for _ in range(4):  # First four sets
        if a >= 25 and b < a and a - b >= 2:
            sets.append((25, b))
            a -= 25
        elif b >= 25 and a < b and b - a >= 2:
            sets.append((a, 25))
            b -= 25
        else:
            return "Impossible"
    if a >= 15 and b < a and a - b >= 2:  # Fifth set
        sets.append((15, b))
        a -= 15
    elif b >= 15 and a < b and b - a >= 2:
        sets.append((a, 15))
        b -= 15
    else:
        return "Impossible"
    if a > 0 or b > 0:  # Extra points after the match should not be left
        return "Impossible"
    a_wins = sum(1 for set_score in sets if set_score[0] > set_score[1])
    b_wins = len(sets) - a_wins
    if a_wins < 3 and b_wins < 3:  # Not enough sets won to finish the match
        return "Impossible"
    return f"{a_wins}:{b_wins} " + " ".join(f"{s[0]}:{s[1]}" for s in sets)

# Read input and process each match
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    result = volleyball_match_score(a, b)
    print(result)
