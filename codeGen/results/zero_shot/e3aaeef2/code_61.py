def count_length(n, m):
    if n == 0:
        return 1
    fixed_point = 9 * (m % 9) + (n // 10)
    operations = min(m, len(str(fixed_point)) - 1)
    return len(str(int((n + m) % 1000000007))) % 1000000007

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_length(n, m))
