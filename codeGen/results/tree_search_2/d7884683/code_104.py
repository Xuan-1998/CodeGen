from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    dp = defaultdict(bool)

    for i in range(n - 1, -1, -1):
        total = sum(arr[:i + 1])
        if total == sum(arr[i:]):
            dp[i] = True
        else:
            dp[i] = False

    partitions = 0
    for i in range(n - 2, -1, -1):
        if dp[i]:
            partitions += 1
            while i > 0 and dp[i - 1]:
                i -= 1

    return partitions


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))

if __name__ == "__main__":
    main()
