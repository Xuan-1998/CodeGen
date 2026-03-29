def solve():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        signs = list(input())
        prefix_sums = preprocess_signs(signs)
        for _ in range(q):
            l, r = map(int, input().split())
            print(process_query(prefix_sums, l - 1, r))

solve()
