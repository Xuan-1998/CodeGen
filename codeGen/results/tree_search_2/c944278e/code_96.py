from sys import stdin

def find_winning_teams(n):
    # Initialize a dictionary to store the memoized results
    memo = {0: [""], 1: ["0", "1"]}

    for i in range(2, n+1):
        new_memo = {}
        for j in range(i):
            # Generate all possible combinations of the previous phases
            prev_combinations = memo[j]
            # Add the current phase to each combination
            for combo in prev_combinations:
                new_combo = "0" + combo if s[j-1] == '0' else "1" + combo
                # Update the new_memo dictionary with the winning teams
                new_memo.setdefault(len(combo), []).append(new_combo)
        memo.update(new_memo)

    return sorted(memo[n])

n = int(stdin.readline())
s = stdin.readline().strip()
print("\n".join(find_winning_teams(n)))
