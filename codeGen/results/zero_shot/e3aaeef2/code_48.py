t = int(input())  # read the number of test cases

for _ in range(t):
    n, m = map(int, input().split())
    n = apply_operations(n, m)
    print(get_length(n))
