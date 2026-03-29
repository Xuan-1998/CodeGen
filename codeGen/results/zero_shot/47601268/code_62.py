def generate_binary_strings(n):
    result = []
    for i in range(1 << n):  # iterate over all numbers less than or equal to 2^n - 1
        bin_str = bin(i)[2:]  # convert integer to binary string, removing '0b' prefix
        if not any(bin_str[i] == bin_str[i-1] for i in range(1, len(bin_str))):  # check for consecutive ones
            result.append(bin_str)
    return result

# Example usage:
n = int(input())
binary_strings = generate_binary_strings(n)
print(len(binary_strings))
