for j in range(i):
    if s[j] == k and team_skill_level <= k:
        new_teams = dp(j, not k)
        result.extend([(k, t) for t in new_teams])
