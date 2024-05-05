python
def max_bitwise_or(n, s):
    # Step 1: Generate all possible substrings of binary string s
    all_substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            all_substrings.add(substring)

    # Step 2: Calculate the bitwise OR of each pair of substrings
    max_or_value = 0
    for substring1 in all_substrings:
        for substring2 in all_substrings:
            if len(substring1) > 0 and len(substring2) > 0:
                or_value = int(substring1, 2) | int(substring2, 2)
                max_or_value = max(max_or_value, or_value)

    # Step 3: Convert the maximum OR value to binary representation
    max_or_binary = bin(max_or_value)[2:]

    return max_or_binary

n = int(input())
s = input()
print(max_bitwise_or(n, s))
