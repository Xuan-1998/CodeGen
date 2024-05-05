def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        pos_count = sum(signs[i] == '+' for i in range(l-1, r))
        neg_count = len(signs) - pos_count
        print(min(pos_count, neg_count))

if __name__ == "__main__":
    solve()
