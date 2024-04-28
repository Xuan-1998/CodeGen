n = int(input())
s = input()

winning_teams = []
skill_levels = [i for i in range(2**n)]

for i in range(n):
    left, right = 0, 2**n
    while left < right:
        mid = (left + right) // 2
        if s[i] == '1':
            winning_teams.append(skill_levels[mid])
            right = mid
        else:
            left = mid + 1

print(*sorted(winning_teams))
