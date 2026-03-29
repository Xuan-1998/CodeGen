def solve():
    t = int(input())
    memo = {}

    for _ in range(t):
        n, m = map(int, input().split())
        val = n

        for _ in range(m):
            last_digit = val % 10
            if last_digit < 9:
                val += 1
            else:
                val //= 10
                val += 1
            state = (val.bit_length(), last_digit)
            if state not in memo:
                memo[state] = []
            memo[state].append(val.bit_length())

        print(sum(length % 1000000007 for length in memo[(n.bit_length(), n % 10)]))

solve()
