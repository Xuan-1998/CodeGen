def simulate_sequence(a):
    memo = {}
    result = []

    for x in range(1, len(a) + 1):
        y = 0
        while True:
            if (x, y) in memo:
                break
            memo[(x, y)] = (y + a[x], x - a[x])

            y += a[x]
            x -= a[x]

            if x <= 0 or x > len(a):
                result.append(y)
                break

    return result

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the results
for i in range(1, n + 1):
    result = simulate_sequence(list(range(2, i + 1)) + a)
    print(result[0] if len(result) > 0 else -1)
