def max_bitwise_or(n, s):
    max_val = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub1 = int(s[i:j], 2)
            for k in range(len(s)):
                for end in range(k + 1, len(s) + 1):
                    sub2 = int(s[k:end], 2)
                    or_val = sub1 | sub2
                    max_val = max(max_val, or_val)
    return bin(max_val)[2:]

# Example usage:
n = int(input())  # read the length of the binary string from stdin
s = input()  # read the binary string from stdin
print(max_bitwise_or(n, s))  # print the maximum possible value in binary representation without leading zeroes
