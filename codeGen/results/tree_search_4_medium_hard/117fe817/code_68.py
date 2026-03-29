def count_digit_one(n):
    cnt = 0
    for i in range(1, n+1):
        if str(i).count('1') > 0:
            cnt += 1
    return cnt

n = int(input())
print(count_digit_one(n))
