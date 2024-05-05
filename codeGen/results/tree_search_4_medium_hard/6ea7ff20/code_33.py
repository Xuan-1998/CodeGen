def can_merge(p):
    n = len(p) // 2

    dp = {(i, j): False for i in range(n+1) for j in range(2)}

    def merge(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        if i == 0 and j == 0:
            return True if p else False

        if p[i-1] < p[j]:
            dp[(i, j)] = merge(i-1, j)
        elif p[i-1] > p[j]:
            dp[(i, j)] = merge(i, j-1)
        else:
            # If the current elements in p are equal, we can't merge
            dp[(i, j)] = False

        return dp[(i, j)]

    for i in range(n+1):
        if not merge(i, 0) or not merge(0, i):
            return "NO"

    return "YES"


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = [int(x) for x in input().split()]
        print("YES" if can_merge(p) else "NO")


if __name__ == "__main__":
    main()
