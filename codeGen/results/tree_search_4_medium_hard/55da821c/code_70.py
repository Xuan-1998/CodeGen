import sys

def min_rearrangements(n, m, plants):
    memo = {}
    for i in range(m):
        memo[i] = [0, 0]

    for i in range(n):
        s, _ = plants[i]
        if not memo[s-1][s-1]:
            # Calculate the minimum number of rearrangements
            move_to_new_section = min_rearrangements(i, m, plants) + 1
            stay_in_original_section = memo[s-1][s-1][0] + (i - memo[s-1][s-1][1])
            if s > 1:
                # Try to merge the current species with the previous one
                prev_species = s - 1
                while prev_species and not plants[i-1][0] == prev_species:
                    i -= 1
                if i > 0:
                    stay_in_original_section = min(stay_in_original_section, move_to_new_section + i)
            memo[s-1] = [min(move_to_new_section, stay_in_original_section), i]

    return memo[m-1][0]

n, m = map(int, sys.stdin.readline().split())
plants = [(int(sys.stdin.readline()), float(sys.stdin.readline())) for _ in range(n)]

print(min_rearrangements(n, m, plants))
