def solve():
    n, q = map(int, input().split())
    signs = [1 if c == '+' else -1 for c in input()]
    result = []

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = sum(signs[i] for i in range(l-1))
        right_sum = sum(signs[i] for i in range(r))

        while left_sum + signs[l-1] == 0:
            left_sum -= signs[l-1]
            l += 1

        while right_sum - signs[r-1] == 0:
            right_sum += signs[r-1]
            r -= 1

        result.append(min(l-r+1, len(signs)-l))

    for res in result:
        print(res)

if __name__ == '__main__':
    solve()
