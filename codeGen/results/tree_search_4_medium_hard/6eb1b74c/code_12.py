def min_steps_to_color_all_letters(text: str, string_set: list) -> tuple:
    n = len(string_set)
    dp = [float('inf')] * (len(text) + 1)
    last_used_index = -1

    for i in range(1, len(text) + 1):
        if text[i-1] not in ''.join(string_set):  # If current char is not in any string
            dp[i] = min(dp[i-1], dp[last_used_index] + 1)
        else:
            last_used_index = i - 1
            for j, s in enumerate(string_set):
                if text[i-1:i+len(s)-1] == s:  # If current char is part of a string
                    last_used_index = i + len(s) - 1
                    break
            dp[i] = min(dp[i-1], dp[last_used_index] + 1)

    if dp[-1] == float('inf'):
        return -1, []
    else:
        steps = dp[-1]
        used_strings = []
        i = len(text) - 1
        for _ in range(steps):
            used_strings.append((i % n, i // n))
            i -= (n + 1)
        return steps, used_strings[::-1]

# Example usage:
text = input().strip()
n = int(input())
string_set = [input().strip() for _ in range(n)]

min_steps, used_strings = min_steps_to_color_all_letters(text, string_set)

if min_steps == -1:
    print(-1)
else:
    print(min_steps)
    for step in used_strings:
        print(*step)
