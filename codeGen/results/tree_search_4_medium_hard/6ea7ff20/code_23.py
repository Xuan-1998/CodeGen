def mergeable(n, p):
    memo = {}

    def mergeable_recursive(i):
        if i >= n:  # base case
            return True

        if (i, len(p) - i) in memo:
            return memo[(i, len(p) - i)]

        left_half = p[:i]
        right_half = p[i:]

        if left_half and right_half and min(left_half) < max(right_half):
            merged = mergeable_recursive(i - 1)
            if not merged:
                return False
            left_half, right_half = right_half, left_half

        memo[(i, len(p) - i)] = (left_half + right_half == p)

        return memo[(i, len(p) - i)]

    return "YES" if mergeable_recursive(n) else "NO"


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES" if mergeable(n, p) else "NO")


if __name__ == "__main__":
    solve()
