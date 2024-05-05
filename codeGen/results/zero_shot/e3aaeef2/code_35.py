t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(find_length_after_operations(n, m))
