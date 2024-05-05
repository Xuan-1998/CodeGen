from collections import defaultdict

def calculate_y(n, sequence):
    memo = defaultdict(int)

    def recursive_calculate(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if x <= 0 or x > n:
            return -1
        a_x = sequence[x-2]
        if a_x > n:
            y_new = y + a_x
            x_new = x - a_x
            result = recursive_calculate(x_new, y_new)
            memo[(x, y)] = result
            return result
        else:
            y_new = y + a_x
            x_new = x + a_x
            result = recursive_calculate(x_new, y_new)
            if result == -1:
                return -1
            memo[(x, y)] = result
            return result

    results = []
    for i in range(2, n+1):
        result = recursive_calculate(i, 0)
        results.append(str(result))
    return '\n'.join(results)

n = int(input())
sequence = list(map(int, input().split()))
print(calculate_y(n, sequence))
