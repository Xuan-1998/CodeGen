def can_form_sum(n):
    max_2020s = n // 2020
    remainder = n % 2020
    return "YES" if remainder <= max_2020s else "NO"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(can_form_sum(n))
