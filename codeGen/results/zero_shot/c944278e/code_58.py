n = int(input())
s = input()
winners = []

for i in range(2**n):
    winner_team = 0
    for j in range(n):
        if (i & (1 << j)) and s[j]:
            winner_team += 1 << j
    winners.append(winner_team)

print(*sorted(winners))
