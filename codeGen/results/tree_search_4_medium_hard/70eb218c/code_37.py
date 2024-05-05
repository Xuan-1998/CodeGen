def min_operations(n, x):
    # Base case: n=1
    if n == 1:
        return -1 if len(str(x)) > 1 else 0

    memo = {}

    def rec_state(state):
        nonlocal memo
        if state in memo:
            return memo[state]
        if state[0] == 1:  # Last digit is 0, no op needed
            result = 0
        else:
            last_digit = int(str(x)[-1])
            for y in range(10):
                if (y != last_digit and x * 10 + y) % (10 ** n) == x:
                    result = min(result, rec_state((n - 1, x * 10 + y)) + 1)
        memo[state] = result
        return result

    return rec_state((n, x))

if __name__ == "__main__":
    import sys
    n, x = map(int, sys.stdin.readline().split())
    print(min_operations(n, x))
