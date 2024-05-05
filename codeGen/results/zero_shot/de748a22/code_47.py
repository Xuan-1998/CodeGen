def solve():
    n, q = map(int, input().split())
    signs = list(input())
    for _ in range(q):
        l, r = map(int, input().split())
        initial_sum = 0
        for i in range(l-1, r):
            if signs[i] == '+':
                initial_sum += 1
            else:
                initial_sum -= 1
        to_remove = sum(1 for sign in signs[l-1:r] if sign != signs[0])
        print(min(to_remove, abs(initial_sum)))

if __name__ == '__main__':
    solve()
