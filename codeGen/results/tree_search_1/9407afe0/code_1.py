def is_set_score_possible(a, b, is_final_set):
    if is_final_set:
        return (a >= 15 or b >= 15) and abs(a - b) >= 2
    else:
        return (a >= 25 or b >= 25) and abs(a - b) >= 2

def main():
    m = int(input().strip())
    for _ in range(m):
        a, b = map(int, input().split())
        
        sets_a, sets_b, set_scores = 0, 0, []
        is_possible = True
        
        # Iterate over each set until one team wins three sets or scores are impossible
        while sets_a < 3 and sets_b < 3 and is_possible:
            is_final_set = (sets_a == 2 and sets_b == 2) or (sets_a + sets_b == 4)
            if is_set_score_possible(a, b, is_final_set):
                set_scores.append((a, b))
                if a > b:
                    sets_a += 1
                else:
                    sets_b += 1
                a, b = 0, 0  # Reset scores for the next set
            else:
                # Check if we can deduct a valid set score from the remaining points
                if not is_final_set and a > 24 and b < a and a - b >= 2:
                    b, a = a - 25, b
                    sets_a += 1
                    set_scores.append((25, a))
                elif not is_final_set and b > 24 and a < b and b - a >= 2:
                    a, b = b - 25, a
                    sets_b += 1
                    set_scores.append((a, 25))
                elif is_final_set and a > 14 and b < a and a - b >= 2:
                    b, a = a - 15, b
                    sets_a += 1
                    set_scores.append((15, a))
                elif is_final_set and b > 14 and a < b and b - a >= 2:
                    a, b = b - 15, a
                    sets_b += 1
                    set_scores.append((a, 15))
                else:
                    is_possible = False
        
        if sets_a == 3 or sets_b == 3:
            print(f"{sets_a}:{sets_b}", ' '.join(f"({x},{y})" for x, y in set_scores))
        else:
            print("Impossible")

if __name__ == "__main__":
    main()
