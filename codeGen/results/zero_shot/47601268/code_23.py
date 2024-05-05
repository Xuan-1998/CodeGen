def has_consecutive_ones(bin):
    bin = str(bin)  
    return any(str(i) + '1' in bin for i in range(len(bin)))

def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        bin_i = str(bin(i))[2:]  
        if not has_consecutive_ones(bin_i):
            count += 1
    return count

n = int(input())  

result = count_numbers_without_consecutive_ones(n)
print(result) 
