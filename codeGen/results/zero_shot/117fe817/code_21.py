def find_digit_one(n):
    count = 0
    for i in range(1, n+1):
        if '1' in str(i):
            count += 1
    return count

n = int(input())
print(find_digit_one(n))
