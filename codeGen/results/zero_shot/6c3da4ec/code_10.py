def max_bitwise_or(s):
    n = len(s)
    prefixes = []
    max_value = 0
    
    for i in range(n):
        prefix = int(''.join(map(str, s[:i+1])), 2)
        prefixes.append(prefix)
        
    for i in range(1, n):
        for j in range(i):
            value = prefixes[i] | prefixes[j]
            max_value = max(max_value, bin(value)[2:].count('1'))
    
    return max_value

n = int(input())
s = input()
print(max_bitwise_or(s))
