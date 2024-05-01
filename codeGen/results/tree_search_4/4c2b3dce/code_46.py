def solution():
    s = input()
    dp = {0: False}
    found_AB = False

    for i, c in enumerate(s):
        if c == 'A':
            new_state = 1 if not found_AB else 2
            if new_state not in dp:
                dp[new_state] = False
            found_AB = True if c == 'B' else False
        elif c == 'B':
            new_state = 2 - (new_state % 2)
            dp[new_state] = True if found_AB and c == 'A' else False

    return "YES" if all(dp.values()) else "NO"

print(solution())
