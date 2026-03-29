def terminate_sequence(a):
    memo = {}
    def helper(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if x <= 0 or x > len(a):
            return -1  # program terminates
        new_x = x + a[x] - 1
        new_y = y + a[x]
        result = helper(new_x, new_y)
        if result == -1:
            return -1
        else:
            memo[(x, y)] = result
            return result
    return [helper(x, 0) for x in range(2, len(a) + 1)]

# Example input
n = int(input())
a = list(map(int, input().split()))

print(*terminate_sequence(a), sep='\n')
