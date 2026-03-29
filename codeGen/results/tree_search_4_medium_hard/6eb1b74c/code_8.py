def min_steps_to_color_all_letters(text, strings):
    n = len(strings)
    m = len(text)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    used_strings = set()

    count = 0

    for i in range(1, m + 1):
        if text[i - 1] not in [s[-1] for s in strings]:
            count += 1
            continue
        for j in range(n):
            if strings[j] in text[i - len(strings[j]):i] and strings[j] not in used_strings:
                dp[i][j + 1] = min(dp[i - 1][j], dp[i - len(strings[j])][j] + 1)
                used_strings.add(strings[j])
                count += 1
        if count == m:
            break

    if count == m:
        return count, [(i, j) for i in range(1, m + 1) for j in range(n) if dp[i][j + 1] > dp[i - 1][j]]
    else:
        return -1
