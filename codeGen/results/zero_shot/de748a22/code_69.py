def solve():
    n, q = map(int, input().split())
    signs = input().split()
    cum_sum = preprocess_signs([int(x) for x in signs])
    for _ in range(q):
        l, r = map(int, input().split())
        print(handle_query(cum_sum, l, r))

if __name__ == "__main__":
    solve()
