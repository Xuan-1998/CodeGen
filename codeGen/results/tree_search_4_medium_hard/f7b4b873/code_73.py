def partition_palindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True

    partitions = []
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                partition = [s[i:j+1]]
                left, right = i, j
                while left > 0 and right < n - 1:
                    if s[left-1] == s[right+1]:
                        left -= 1
                        right += 1
                        partition.append(s[left:right+1])
                    else:
                        break
                partitions.append(partition)

    return partitions


def main():
    s = input()
    partitions = partition_palindromes(s)
    for partition in partitions:
        print(partition)


if __name__ == "__main__":
    main()
