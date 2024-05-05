from collections import defaultdict

def min_steps_to_color_text():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    dp = [[False] * (len(t) + 1) for _ in range(len(t) + 1)]
    used_strings = set()

    for i in range(len(t)):
        for j in range(i, len(t)):
            if all(s in t[i:j+1] for s in strings):
                dp[i][j] = True

    min_steps = float('inf')
    for i in range(len(t)):
        for j in range(i, len(t)):
            if dp[i][j]:
                steps = 0
                used_strings_copy = set(used_strings)
                for k in range(i, j+1):
                    for string in strings:
                        if t[k:k+len(string)] == string and string not in used_strings_copy:
                            used_strings_copy.add(string)
                            steps += 1
                            break
                    if len(used_strings_copy) > 0:
                        break
                min_steps = min(min_steps, steps)

    if min_steps == float('inf'):
        return -1
    else:
        return min_steps

print(min_steps_to_color_text())
