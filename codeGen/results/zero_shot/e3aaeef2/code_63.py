def next_digit(d):
    if d == 9:
        return 1
    else:
        return d + 1

def solve(n, m):
    result = n
    for _ in range(m):
        new_result = ""
        for digit in str(result):
            new_result += str(next_digit(int(digit)))
        result = int(new_result)
    return len(str(result)) % (10**9+7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
