def max_grade(n, t):
    state = [[False] * (t + 1) for _ in range(n + 1)]
    max_grades = [0.0] * (n + 1)

    # Base case: it's always possible to get 0.0 within any time limit
    for j in range(t + 1):
        state[0][j] = True

    for i in range(1, n + 1):
        for j in range(t + 1):
            if j < t:
                # If the current digit is less than or equal to (1/2) * (t - j)
                if float('0.' + '9' * i) <= (1 / 2) * (t - j):
                    state[i][j] = True
                    max_grades[i] = max(max_grades[i], float('0.' + '9' * i))
                else:
                    state[i][j] = False

    # Find the maximum possible grade that can be obtained within t seconds
    max_grade = 0.0
    for j in range(t, -1, -1):
        if state[n][j]:
            max_grade = max(max_grade, float('0.' + '9' * n) + (t - j) / 10**n)
            break

    return round(max_grade, 2)

# Example usage:
n, t = map(int, input().split())
print(max_grade(n, t))
