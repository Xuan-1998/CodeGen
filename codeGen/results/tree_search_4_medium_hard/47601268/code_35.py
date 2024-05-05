def count_binary_representations(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        bi = bin(i)[2:]  # Remove '0b' prefix
        consecutive_ones = False
        for j in range(len(bi) - 1):
            if bi[j] == '1' and bi[j + 1] == '1':
                consecutive_ones = True
                break
        if not consecutive_ones:
            dp[i] = dp[i-1] + 1
        else:
            j = i - 1
            while True:
                bj = bin(j)[2:]  # Remove '0b' prefix
                for k in range(len(bj) - 1):
                    if bj[k] == '1' and bj[k + 1] == '1':
                        break
                else:
                    dp[i] = dp[j]
                    break
                j -= 1

    return dp[n]

n = int(input())
print(count_binary_representations(n))
