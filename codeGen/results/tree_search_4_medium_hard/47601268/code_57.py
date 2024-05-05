def count_numbers(n):
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        has_consecutive_ones = False
        curr_bin = bin(i)[2:]  # Convert to binary and remove '0b' prefix
        for j in range(len(curr_bin) - 1):
            if curr_bin[j] == '1' and curr_bin[j + 1] == '1':
                has_consecutive_ones = True
                break
        dp[i] = not has_consecutive_ones

    return sum(dp)

# Test the function
n = int(input())
print(count_numbers(n))
