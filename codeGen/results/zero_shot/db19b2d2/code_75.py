n = int(input())  # number of players on the team
m = int(input())  # number of departments in the university
h = int(input())  # department of interest
s = [int(x) for x in input().split()]  # list of numbers of basketball players in each department

total_players = sum(s)
min_players_needed = total_players - s[h-1]

probability = min_players_needed / total_players if min_players_needed > 0 else -1
print(probability)
