import sys

def count_binary_numbers(n):
    count = 0
    for i in range(n+1):
        binary = bin(i)[2:]
        if all(x != '1' or x == '1' and y == '0' for x, y in zip(binary, binary[1:])):
            count += 1
    return count

n = int(sys.stdin.read())
print(count_binary_numbers(n))
