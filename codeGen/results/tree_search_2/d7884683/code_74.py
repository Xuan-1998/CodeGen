def max_partitions(arr):
    n = len(arr)
    table = [[0, 0] for _ in range(n + 1)]

    # Base case: when i == 0 or i == n - 1
    table[0][0] = 0
    table[n][0] = 0

    for i in range(1, n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            table[i][0] = 1 + (table[i - 1][0] if i > 0 else 0)
        else:
            table[i][0] = max(table[i - 1][0], table[i - 1][1])
        table[i][1] = table[i - 1][0]

    return table[-1][0]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))


if __name__ == "__main__":
    main()
