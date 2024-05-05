def find_longest_increasing_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    memo = {0: 1}

    for i in range(1, n):
        max_length = 0
        for j in range(i):
            if arr[i] > arr[j]:
                length = memo.get(j, 0) + 1
                max_length = max(max_length, length)
        memo[i] = max_length

    longest_lengths = set(memo.values())
    return len(longest_lengths)


if __name__ == "__main__":
    print(find_longest_increasing_subsequences())
