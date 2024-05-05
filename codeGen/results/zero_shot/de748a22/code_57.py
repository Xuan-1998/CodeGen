def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        total_sign_sum = sum(1 if sign == '+' else -1 for sign in signs[l-1:r])
        remaining_elements_to_remove = abs(total_sign_sum)
        print(remaining_elements_to_remove)

if __name__ == "__main__":
    solve()
