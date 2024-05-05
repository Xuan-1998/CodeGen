def has_consecutive_ones(i):
    while i > 0:
        if (i & 1) == 1:  
            if ((i >> 1) & 1) == 1:  
                return True
        i >>= 1
    return False

def count_numbers(n):
    count = 0
    for i in range(n + 1):
        if not has_consecutive_ones(i):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())  
    print(count_numbers(n))  
