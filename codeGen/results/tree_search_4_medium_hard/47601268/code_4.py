dp = {0: 1}  # base case: 0 has no consecutive ones
def count_valid_binaries(n):
    count = dp.get(0, 0)
    for i in range(1, n+1):  # iterate up to n
        if i % 2 == 0:  # even integer
            count += 1 if not (has_consecutive_ones(bin(i)[2:])) else 0
        else:  # odd integer
            count += dp.get((i-1) // 2, 0)
    return count

def has_consecutive_ones(binary):
    for j in range(len(binary) - 1):  # check all but the last bit
        if binary[j] == '1' and binary[j+1] == '1':
            return True
    return False

n = int(input())  # read input from stdin
print(count_valid_binaries(n))  # print result to stdout
