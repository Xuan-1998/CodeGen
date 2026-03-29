from collections import defaultdict

def min_steps_to_color_text(t, S):
    memo = defaultdict(list)

    def dp(i, colored_chars):
        if (i, tuple(sorted(colored_chars))) in memo:
            return memo[(i, tuple(sorted(colored_chars)))][0]
        
        if i == len(t) - 1:
            return len(t) - sum(1 for c in t[i:] if c not in colored_chars)

        min_steps = float('inf')
        colored_chars_set = set(colored_chars)
        
        for s in S:
            if all(c in colored_chars_set for c in s):
                steps = dp(i + len(s), colored_chars | set(range(i, i + len(s))))
                min_steps = min(min_steps, 1 + steps)

        memo[(i, tuple(sorted(colored_chars)))] = [min_steps]
        return min_steps

    return dp(0, set())

while True:
    try:
        t = input().strip()
        n = int(input())
        S = [input().strip() for _ in range(n)]

        result = min_steps_to_color_text(t, S)

        if result == -1:
            print(-1)
        else:
            steps = result
            used_substrings = []
            i = len(t) - 1

            while steps > 0:
                min_length = float('inf')
                best_s = None
                
                for s in S:
                    if all(c in set(range(i, i + len(s))) for c in range(len(s))):
                        length = len(s)
                        if length < min_length:
                            min_length = length
                            best_s = s

                used_substrings.append((S.index(best_s) + 1, i - min_length + 1))
                steps -= 1
                i -= min_length

            print(result)
            for pair in used_substrings:
                print(*pair)

    except:
        break
