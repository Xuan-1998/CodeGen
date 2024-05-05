def apply_operation(n):
    n_str = str(n)
    result = []
    for digit in n_str:
        result.append(str(int(digit) + 1))
    return int(''.join(result))

def apply_operations(n, m):
    for _ in range(m):
        n = apply_operation(n)
    return n

def calculate_length(n):
    return len(str(n)) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = apply_operations(n, m)
    print(calculate_length(result))
