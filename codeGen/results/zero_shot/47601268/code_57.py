def has_consecutive_ones(binary):
    ones = 0
    for char in binary:
        if char == '1':
            ones += 1
        elif ones > 0:
            return True  # Consecutive ones found!
    return False  # No consecutive ones found

def count_non_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        binary = bin(i)[2:]  # [2:] removes the '0b' prefix
        if not has_consecutive_ones(binary):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())  # Read input from stdin
    result = count_non_consecutive_ones(n)
    print(result)  # Print output to stdout
