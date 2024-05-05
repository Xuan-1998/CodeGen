import math

def calculate_probability(n, m, h, s):
    # Calculate the total number of possible teams
    total_possible_teams = math.factorial(sum(s)) / (math.factorial(h) * math.factorial(sum(s)-h))

    # Calculate the number of teams that contain at least one player from the department of interest
    total_teams_with_at_least_one_player_from_department_of_interest = 0
    for i in range(m):
        if i != h:
            total_teams_with_at_least_one_player_from_department_of_interest += math.factorial(s[i]) / (math.factorial(h) * math.factorial(s[i]-h))
        else:
            total_teams_with_at_least_one_player_from_department_of_interest += 1

    # Calculate the probability
    if n > sum(s):
        return -1
    else:
        return total_teams_with_at_least_one_player_from_department_of_interest / total_possible_teams


n = int(input())
m = int(input())
h = int(input())
s = list(map(int, input().split()))

print(calculate_probability(n, m, h, s))
