def count_binary_numbers(n):
    count = 0
    for i in range(n+1):
        binary_str = bin(i)[2:]
        if not has_consecutive_ones(binary_str):
            count += 1
    return count

def has_consecutive_ones(s):
    if len(s) < 2:
        return False
    for i in range(len(s)-1):
        if s[i] == '1' and s[i+1] == '1':
            return True
    return False

if __name__ == "__main__":
    n = int(input())
    print(count_binary_numbers(n))
