from sys import stdin

def count_non_consecutive Ones(n):
    counter = 0
    dp_state = 0
    
    for i in range(1, n+1):
        bin_str = bin(i)[2:]  # convert integer to binary string
        
        if not dp_state:
            if any(bin_str[j] == '1' and bin_str[j+1] == '1' for j in range(len(bin_str)-1)):
                dp_state = 1
        else:
            counter += 1
    
    return counter

n = int(stdin.readline())
print(count_non_consecutiveOnes(n))
