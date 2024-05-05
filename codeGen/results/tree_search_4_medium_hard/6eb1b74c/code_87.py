import sys

def color_text(t, strings):
    n = len(strings)
    dp = [[0] * (n + 1) for _ in range(len(t) + 1)]
    used_strings = [0] * (n + 1)

    for i in range(1, len(t) + 1):
        if t[i - 1] not in strings[0]:
            dp[i][0] = dp[i - 1][0]
        else:
            min_steps = float('inf')
            for j in range(n + 1):
                if used_strings[j] == 0 and t[i - len(strings[j]):i].startswith(strings[j]):
                    steps = dp[i - len(strings[j])][j] + (1 if j > 0 else 0)
                    min_steps = min(min_steps, steps)
            dp[i][0] = min_steps
        used_strings[0] += (dp[i][0] > dp[i - 1][0])

    min_steps = dp[-1][0]
    if min_steps == float('inf'):
        return -1

    result = []
    i, j = len(t), 0
    while i > 0:
        for string_index in range(n + 1):
            if used_strings[string_index] and t[i - len(strings[string_index]):i].startswith(strings[string_index]):
                result.append((string_index, i - len(strings[string_index])))
                i -= len(strings[string_index])
                used_strings[string_index] = 0
                break

    return min_steps, '\n'.join(map(str, result))

t = input()
n = int(input())
strings = [input() for _ in range(n)]
min_steps, result = color_text(t, strings)
print(min_steps)
print(result)
