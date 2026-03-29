import sys

def count_binary_no_consecutive_ones(n):
    def generate_binary_numbers(k, n, prefix, count):
        if k > 0:
            prefix += '1' if (n >> k) & 1 else '0'
            count = generate_binary_numbers(k-1, n-1, prefix, count)
            return 1 + count
        elif k < 0:
            return count
        else:
            for i in range(2):
                prefix += str(i)
                if int(prefix, 2) <= n:
                    global count_no_consecutive_ones
                    count = generate_binary_numbers(-1, -1, '', 0)
                    if int(prefix, 2) < n and (bin(int(prefix, 2))[2:].count('1') == bin(n)[2:].count('1')):
                        count += 1
            return count

    count_no_consecutive_ones = generate_binary_numbers(30, n, '', 0)
    return count_no_consecutive_ones

n = int(input())
print(count_binary_no_consecutive_ones(n))
