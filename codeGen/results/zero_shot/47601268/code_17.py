def count_binary_no_consecutive_ones(n):
    def check_binary(k):
        bin_k = bin(k)[2:]
        has_consecutive_ones = False
        for i in range(len(bin_k) - 1):
            if bin_k[i] == '1' and bin_k[i+1] == '1':
                has_consecutive_ones = True
                break
        return not has_consecutive_ones

    count = 0
    for k in range(n + 1):
        if check_binary(k):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    print(count_binary_no_consecutive_ones(n))
