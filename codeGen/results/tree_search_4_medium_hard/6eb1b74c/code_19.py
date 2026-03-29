from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    dp = [[0] * (len(t) + 1) for _ in range(len(t) + 1)]
    used_strings = defaultdict(set)

    for i in range(1, len(t) + 1):
        for j in range(i - 1, -1, -1):
            if t[j:] in s:
                string_index = [k for k, x in enumerate(s) if x == t[j:]][0]
                used_strings[string_index].add(j)
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                while j < len(t) and t[j:] in s:
                    string_index = [k for k, x in enumerate(s) if x == t[j:]][0]
                    used_strings[string_index].add(j)
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            else:
                dp[i][j] = dp[i-1][j]

    min_steps = dp[-1][-1]
    steps_taken = []
    i, j = len(t), -1
    while i > 0:
        for string_index in list(used_strings.keys()):
            if t[j:] in s[string_index]:
                used_strings[string_index].remove(j)
                steps_taken.append((string_index + 1, j))
                break
        else:
            j -= 1

    if min_steps == -1 or (len(t) > 0 and t[0] not in ''.join([s[i-1] for i, _ in sorted(steps_taken)])):
        print(-1)
    else:
        print(min_steps)
        for step, pos in sorted(steps_taken):
            print(step, pos)

if __name__ == '__main__':
    solve()
