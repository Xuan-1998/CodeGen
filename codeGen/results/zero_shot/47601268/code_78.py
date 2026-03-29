def count_binary_no_consecutive_ones(n):
    count = 0
    for i in range(2**n):  # iterate over all possible integers <= n
        bin_i = bin(i)[2:]  # get the binary representation of i
        if not any('11' in bin_i[j:j+2] for j in range(len(bin_i)-1)):  # check if no consecutive ones
            count += 1
    return count

n = int(input())  # read input from stdin
print(count_binary_no_consecutive_ones(n))  # print the result to stdout
