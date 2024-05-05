===BEGIN CODE===
from collections import deque
def color_text(t, substrings):
    n = len(t)
    memo = {}
    def dp(i, substrings):
        if (i, tuple(substrings)) in memo:
            return memo[(i, tuple(substrings))]
        if not substrings:
            return 0
        steps = float('inf')
        for j, substring in enumerate(substrings):
            if t[i:].startswith(substring):
                res = dp(i + len(substring), substrings[:j] + substrings[j+1:])
                steps = min(steps, res + 1)
        memo[(i, tuple(substrings))] = steps
        return steps
    result = dp(0, substrings)
    if result == float('inf'):
        print(-1)
    else:
        queue = deque([(result, 0)])
        while queue:
            steps, pos = queue.popleft()
            for j, substring in enumerate(substrings):
                if t[pos:].startswith(substring):
                    new_steps = steps - 1
                    new_pos = pos + len(substring)
                    if new_steps == 0:
                        break
                    queue.append((new_steps, new_pos))
                    substrings.pop(j)
                    break
        print(result)
        while result > 0:
            for j, substring in enumerate(substrings):
                if t[queue[-1][1]-len(substring):].startswith(substring):
                    print(f"{j+1} {queue.pop()[1] - len(substring)}")
                    result -= 1
                    break

===END CODE===
