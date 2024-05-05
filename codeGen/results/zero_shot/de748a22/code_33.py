def solve():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(input())
        prefix_sum = preprocess_array(arr)
        for _ in range(q):
            l, r = map(int, input().split())
            print(handle_query(prefix_sum, l-1, r))
