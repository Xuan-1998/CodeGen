def min_changes(s):
    n = len(s)
    k = 6
    if n % k != 0:
        s += 'RGB' * ((n + k - 1) // k)

    count = [s.count('R'), s.count('G'), s.count('B')]
    target_count = [k // 3, k // 3, k // 3]

    diff = sum(abs(a - b) for a, b in zip(count, target_count))
    return min(diff, n - k)

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s))
