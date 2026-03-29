def can_form_polygon(knights):
    memo = {}

    def dp(i, good_knights):
        if (i, good_knights) in memo:
            return memo[(i, good_knights)]

        if i == 0:
            return True

        if not knights[i - 1] and good_knights > 0:
            return False

        bad_knights = good_knights
        for j in range(i):
            if knights[j]:
                bad_knights -= 1
                break

        result = dp((i - 1) % len(knights), bad_knights)
        memo[(i, good_knights)] = result
        return result

    return "YES" if dp(len(knights), sum(knights)) else "NO"


def main():
    n = int(input())
    knights = list(map(int, input().split()))
    print(can_form_polygon(knights))


if __name__ == "__main__":
    main()
