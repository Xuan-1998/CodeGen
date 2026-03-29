def count_digit1s(n):
    memo = {0: 0}  # base case: count for 0 is 0

    def helper(k):
        if k not in memo:
            if k == 0:  # handle edge case where k is 0
                memo[k] = 0
            elif k < 10:  # consider only the last digit
                memo[k] = int(str(k) != '1')
            else:
                last_digit = k % 10
                if last_digit == 1:
                    memo[k] = helper(k // 10) + (k >= 2 and k <= n)
                elif last_digit > 1:
                    memo[k] = helper(k // 10) + 1
                else:  # last digit is 0
                    memo[k] = helper(k // 10)
        return memo[k]

    total_count = 0
    for i in range(n + 1):
        total_count += helper(i)

    return total_count

n = int(input())  # read input from stdin
print(count_digit1s(n))  # print answer to stdout
