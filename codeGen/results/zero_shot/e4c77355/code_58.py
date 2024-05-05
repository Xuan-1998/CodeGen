def longest_increasing_subsequence(sequence):
    if not sequence:
        return 0

    lis = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)

# Read the input from standard input
sequence = [int(num) for num in input().split()]

print(longest_increasing_subsequence(sequence))
