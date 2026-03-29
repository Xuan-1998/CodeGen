memo = {}

def find_min_x(a, b):
    if a < 0 or b < 0:
        return -1
    if (a, b) in memo:
        return memo[(a, b)]
    min_x = float('inf')
    for x in range(a + 1):
        y = a - x
        if x ^ y == b:
            min_x = min(min_x, x)
    memo[(a, b)] = min_x
    return min_x

def solve():
    A = int(input())
    B = int(input())
    X = find_min_x(A, B)
    if X == float('inf'):
        print(-1)
    else:
        Y = A - X
        print(X, Y)

solve()
