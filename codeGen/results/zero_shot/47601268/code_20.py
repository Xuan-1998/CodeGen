def count_binary(n):
    count = 0
    for i in range(n+1):
        has_consecutive_ones = False
        binary = bin(i)[2:]
        for j in range(len(binary)-1):
            if binary[j] == '1' and binary[j+1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())
print(count_binary(n))
