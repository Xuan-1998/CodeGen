def is_sum_possible(n):
    b = n % 2020
    a_plus_b = n // 2020
    return b <= a_plus_b

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print("YES" if is_sum_possible(n) else "NO")
