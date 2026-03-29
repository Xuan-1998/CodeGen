import sys

n = int(sys.stdin.readline())
count = 0
i = 1

while i <= n:
    is_valid = True
    prev_bit = None
    num_str = bin(i)[2:]
    
    for bit in num_str:
        if prev_bit == '1' and bit == '1':
            is_valid = False
            break
        prev_bit = bit
    
    if is_valid:
        count += 1
    
    i += 1

print(count)
