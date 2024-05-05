def count_ones(n):
    # Initialize memo dictionary
    memo = {0: 0, 1: 1}

    for i in range(2, n.bit_length() + 1):
        if i not in memo:
            memo[i] = (n // (10 ** i)) * (10 ** (i - 1) - 9) + 1

    return sum(memo.values())

if __name__ == "__main__":
    n = int(input())
    print(count_ones(n))
