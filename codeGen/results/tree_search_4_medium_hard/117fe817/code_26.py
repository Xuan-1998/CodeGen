def find_count_of_ones(n):
    ones_counts = {i: 0 for i in range(10)}
    
    for i in range(n + 1):
        for j in str(i):
            if j == '1':
                ones_counts[int(j)] += 1
    
    return sum(counts.values())

n = int(input())
print(find_count_of_ones(n))
