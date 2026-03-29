import sys

def count_non_consecutive(n):
    dp_state = [False] * (n + 1)
    dp_state[0] = True
    dp_state[1] = True
    
    for i in range(2, n + 1):
        bin_str = bin(i)[2:]
        has_consecutive_ones = False
        count = 0
        for j in range(len(bin_str)):
            if bin_str[j] == '1':
                count += 1
                if count > 1 and bin_str[j - 1] == '1':
                    has_consecutive_ones = True
                    break
            else:
                count = 0
        dp_state[i] = not has_consecutive_ones
    
    count = 0
    for i in range(2, n + 1):
        if dp_state[i]:
            count += 1
    
    return count

n = int(sys.stdin.readline())
print(count_non_consecutive(n))
