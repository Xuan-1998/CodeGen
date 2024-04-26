def possible_scores(a, b, last_set):
    scores = []
    for i in range(0, min(a, b) + 1):
        if last_set:
            if (a - i >= 15 and b == i) or (b - i >= 15 and a == i):
                scores.append((a - i, i))
        else:
            if (a - i >= 25 and b == i) or (b - i >= 25 and a == i):
                scores.append((a - i, i))
            elif (a - i >= 25 and a - i <= b + 2) or (b - i >= 25 and b - i <= a + 2):
                scores.append((a - i, i))
    return scores

def find_best_match_score(a, b):
    for total_sets in range(3, 6):
        for a_wins in range(max(0, total_sets - 3), min(3, total_sets) + 1):
            b_wins = total_sets - a_wins
            if a_wins < 3 and b_wins < 3:
                continue
            for fifth_set in [False, True]:
                a_remaining, b_remaining = a, b
                a_sets, b_sets = 0, 0
                set_scores = []
                for _ in range(total_sets - 1):
                    for score in possible_scores(a_remaining, b_remaining, False):
                        a_score, b_score = score
                        if a_score > b_score:
                            a_sets += 1
                        else:
                            b_sets += 1
                        a_remaining -= a_score
                        b_remaining -= b_score
                        set_scores.append(score)
                        break
                for score in possible_scores(a_remaining, b_remaining, fifth_set):
                    a_score, b_score = score
                    if a_score > b_score:
                        a_sets += 1
                    else:
                        b_sets += 1
                    set_scores.append(score)
                    if a_sets == a_wins and b_sets == b_wins:
                        return f"{a_sets}:{b_sets} " + " ".join(f"{x}:{y}" for x, y in set_scores)
    return "Impossible"

# Read input and process each match
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(find_best_match_score(a, b))
