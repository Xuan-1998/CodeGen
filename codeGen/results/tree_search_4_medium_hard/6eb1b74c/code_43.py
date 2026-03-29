import sys

def solve():
    t = input().strip()
    n = int(input())
    strings = [input() for _ in range(n)]

    dp = [[float('inf')] * (len(t) + 1) for _ in range(len(t) + 1)]
    dp[0][0] = 0

    min_steps = float('inf')
    last_occurrence = {}

    for i in range(1, len(t) + 1):
        for j in range(1, len(t) + 1):
            if t[i-1] == strings[-1]:
                dp[i][j] = dp[i-1][j]
            else:
                min_steps_to_color_current_letter = float('inf')
                for k in range(n):
                    last_occurrence_of_s_k = last_occurrence.get(k, -1)
                    if j > last_occurrence_of_s_k and t[i-1] == strings[k][-1]:
                        steps_to_color_current_letter = dp[last_occurrence_of_s_k][i-1] + 1
                        min_steps_to_color_current_letter = min(min_steps_to_color_current_letter, steps_to_color_current_letter)
                dp[i][j] = min_steps_to_color_current_letter

            if i < len(t):
                last_occurrence[len(s)-1] = j

    if min_steps == float('inf'):
        return -1
    else:
        current_index = len(t)
        result = []
        while min_steps > 0:
            for k in range(n):
                if t[current_index-1] == strings[k][-1]:
                    result.append((k, last_occurrence.get(k, -1)))
                    min_steps -= 1
                    break
            current_index -= 1

    print(min_steps)
    for step in result:
        print(*step)

solve()
