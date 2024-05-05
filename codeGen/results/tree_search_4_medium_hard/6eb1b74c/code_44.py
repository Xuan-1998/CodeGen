def min_steps_to_color_all(text, strings):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(text):
            return 0

        steps = float('inf')
        for k in range(j, -1, -1):
            pos = text.find(strings[k], i)
            if pos != -1:
                steps = min(steps, dp(pos + len(strings[k]), k) + 1)

        memo[(i, j)] = steps
        return steps

    result = float('inf')
    for j in range(len(strings)):
        result = min(result, dp(0, j) + 1)

    if result == float('inf'):
        return -1

    step_count = result - 1
    used_strings = []
    pos = 0
    for _ in range(step_count):
        for j in range(len(strings)):
            pos = text.find(strings[j], pos)
            if pos != -1:
                used_strings.append(j)
                break

    print(result)
    for i, s in enumerate(used_strings):
        print(f"{s+1} {pos+i}")
