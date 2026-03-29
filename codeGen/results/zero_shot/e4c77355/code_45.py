import sys

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)


def main():
    sequence = []
    for line in sys.stdin:
        for num in map(int, line.strip().split()):
            sequence.append(num)

    print(longest_increasing_subsequence(sequence))


if __name__ == "__main__":
    main()
