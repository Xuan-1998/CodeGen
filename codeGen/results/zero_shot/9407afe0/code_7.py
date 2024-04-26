def is_possible(a, b, set_scores):
    # Check if the scores are possible given the set scores
    a_score, b_score = 0, 0
    for score in set_scores:
        a_score += score[0]
        b_score += score[1]
    return a_score == a and b_score == b

def volleyball_match(a, b):
    # The possible scores for a team to win a set
    possible_scores = [(i, i - 2) for i in range(25, 51)] + [(15, 13), (16, 14), (17, 15), (18, 16), (19, 17), (20, 18), (21, 19), (22, 20), (23, 21), (24, 22)]
    possible_scores += [(j, i) for (i, j) in possible_scores]

    # Iterate over all possible match outcomes
    for a_wins in range(4):
        for b_wins in range(4):
            if a_wins == 3 or b_wins == 3:
                # Generate all possible sets
                for set1 in possible_scores:
                    for set2 in possible_scores:
                        for set3 in possible_scores:
                            for set4 in (possible_scores if a_wins + b_wins > 2 else [(0, 0)]):
                                for set5 in (possible_scores if a_wins + b_wins == 2 else [(0, 0)]):
                                    sets = [set1, set2, set3, set4, set5]
                                    a_sets_won = sum(1 for score in sets if score[0] > score[1])
                                    b_sets_won = sum(1 for score in sets if score[1] > score[0])
                                    if a_sets_won == a_wins and b_sets_won == b_wins and is_possible(a, b, sets):
                                        # Format the output
                                        sets = [f"{score[0]}:{score[1]}" for score in sets if score != (0, 0)]
                                        return f"{a_wins}:{b_wins} " + " ".join(sets)
    return "Impossible"

# Read the number of matches
m = int(input())

# Process each match
for _ in range(m):
    a, b = map(int, input().split())
    print(volleyball_match(a, b))
