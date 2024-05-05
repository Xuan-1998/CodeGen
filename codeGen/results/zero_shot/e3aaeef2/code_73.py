def apply_operation(n):
    result = ''
    for digit in str(n):
        new_digit = str(int(digit) + 1)
        result += new_digit
    return int(result)

def apply_m_operations(n, m):
    if m == 0:
        return n
    else:
        return apply_m_operations(apply_operation(n), m - 1)

def solve(n, m):
    result = apply_m_operations(n, m)
    return len(str(result)) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
