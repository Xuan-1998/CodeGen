def isValid(knights):
    n = len(knights)
    dp = [False] * (n + 1)
    k = 0

    for i in range(n):
        if knights[i]:
            k += 1
        else:
            k -= 1
        dp[k] = True

    return "YES" if dp[n] else "NO"


def main():
    n = int(input())
    knights = list(map(int, input().split()))
    print(isValid(knights))


if __name__ == "__main__":
    main()
