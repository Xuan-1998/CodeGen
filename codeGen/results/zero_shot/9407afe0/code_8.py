def is_valid_set(a, b, is_final_set):
    min_points = 15 if is_final_set else 25
    return (a >= min_points or b >= min_points) and abs(a - b) >= 2

def generate_possible_scores(a, b):
    possible_scores = []
    for sets_count in range(3, 6):  # From 3 to 5 sets
        # Use itertools.product to generate possible scores
        for scores in itertools.product(range(0, max(a, b) + 1), repeat=sets_count):
            if sum(scores[0::2]) == a and sum(scores[1::2]) == b:
                possible_scores.append(scores)
    return possible_scores

def find_best_match_score(a, b):
    possible_scores = generate_possible_scores(a, b)
    best_score = "Impossible"
    for scores in possible_scores:
        valid = True
        team_a_wins = 0
        opponent_wins = 0
        for i in range(len(scores) // 2):
            team_a_score = scores[2 * i]
            opponent_score = scores[2 * i + 1]
            if not is_valid_set(team_a_score, opponent_score, i == (len(scores) // 2 - 1)):
                valid = False
                break
            if team_a_score > opponent_score:
                team_a_wins += 1
            else:
                opponent_wins += 1
        if valid and team_a_wins == 3 and (best_score == "Impossible" or opponent_wins < int(best_score[2])):
            best_score = f"{team_a_wins}:{opponent_wins}"
    return best_score

# Read the number of matches
m = int(input().strip())

# Process each match
for _ in range(m):
    a, b = map(int, input().strip().split())
    print(find_best_match_score(a, b))
