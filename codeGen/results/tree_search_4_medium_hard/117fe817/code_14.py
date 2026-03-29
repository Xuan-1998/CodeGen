def findOnes(n):
    ones = [0] * (n.bit_length() + 1)
    
    for i in range(1, n.bit_length() + 1):
        start = 2 ** (i - 1) if i > 0 else 0
        end = 2 ** i
        
        for j in range(start, end):
            ones[i] += str(j).count('1')
    
    return sum(ones)

n = int(input())
print(findOnes(n))
