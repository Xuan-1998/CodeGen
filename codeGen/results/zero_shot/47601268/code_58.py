def has_consecutive_ones(binary_str):
    for i in range(len(binary_str) - 1):
        if binary_str[i] == '1' and binary_str[i+1] == '1':
            return True
    return False

def count_non_consecutive_ones(n):
    count = 0
    for i in range(2**n):  # Generate all possible binary strings of length n
        binary_str = bin(i)[2:].zfill(n)  # Convert integer to binary string and pad with zeros
        if not has_consecutive_ones(binary_str):  # Check if the string has consecutive ones
            count += 1
    return count

def main():
    n = int(input())  # Read input from stdin
    print(count_non_consecutive_ones(n))  # Call the helper function and print the result

if __name__ == '__main__':
    main()
