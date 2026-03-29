def solve():
    n, q = map(int, input().split())
    signs = list(input())

    cumulative_sum = [0] * (n + 1)
    for i in range(n):
        cumulative_sum[i+1] = cumulative_sum[i] + (1 if signs[i] == '+' else -1)

    result = []
    for _ in range(q):
        l, r = map(int, input().split())
        prefix_sum = cumulative_sum[r]
        suffix_sum = cumulative_sum[l-1]

        remaining_sum = prefix_sum - suffix_sum
        if remaining_sum > 0:
            result.append(r-l+1)
        elif remaining_sum < 0:
            result.append(-remaining_sum)
        else:
            result.append(0)

    for num in result:
        print(num)

solve()
