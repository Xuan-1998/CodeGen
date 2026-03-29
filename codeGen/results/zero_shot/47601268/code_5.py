def has_consecutive_ones(n):
    bin_n = bin(n)[2:]
    return any('11' in bin_n[i:i+2] for i in range(len(bin_n)-1))

def count_binary_representations(n):
    count = 0
    for i in range(n+1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(input())
print(count_binary_representations(n))
