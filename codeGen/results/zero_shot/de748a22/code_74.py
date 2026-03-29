def solution():
    n, q = map(int, input().split())
    signs = list(input())

    total_positive = sum(1 for sign in signs if sign == '+')
    total_negative = len(signs) - total_positive

    for _ in range(q):
        l, r = map(int, input().split())
        positive_in_range = sum(1 for i in range(l-1, r) if signs[i] == '+')
        negative_in_range = r - l + 1 - positive_in_range

        removed_positive = max(0, total_positive - positive_in_range)
        removed_negative = max(0, total_negative - negative_in_range)

        print(min(removed_positive, removed_negative))

solution()
