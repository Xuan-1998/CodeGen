def f(n, t):
    if n == 0:
        return 0

    # Base case: if we've exceeded the time limit, return 0
    if t < 1:
        return 0

    # Recursively explore two options: round or don't round
    without_rounding = f(n-1, t-1)
    with_rounding = round(9.99 * (10**n)) + f(n-1, t-int((t-1) / len(str(9.99 * (10**n)))) - 1)

    return max(without_rounding, with_rounding)


n, t = map(int, input().split())
print(f(n, t))
