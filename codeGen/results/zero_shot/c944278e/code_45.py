n = int(input())
s = input()
winning_teams = [0]
for i in range(1, 2**n):
    if bin(i).count('1') == s.count('1'):
        winning_teams.append(i)
print(*sorted(winning_teams))
