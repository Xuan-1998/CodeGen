def expected_carries(A, B):
    N = len(str(max(A, B)))
    memo = {}

    def dp(n, carry):
        if (n, carry) in memo:
            return memo[(n, carry)]
        if n == 0:
            return 0

        next_carry = False
        for i in range(N - 1, -1, -1):
            a_digit = int(str(A)[i])
            b_digit = int(str(B)[i])
            if (a_digit >= b_digit and carry) or (b_digit > a_digit):
                next_carry = True
                break

        result = dp(n - 1, next_carry)
        memo[(n, carry)] = result
        return result

    total_carries = 0
    for i in range(N + 1):
        total_carries += dp(i, False)

    return total_carries / (N ** 2)
