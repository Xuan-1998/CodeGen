def count_digit_one(n):
    total = 0
    for i in range(30):  # 30 is enough to cover all digit positions up to n
        if i == 0:  # ones place
            total += n + 1
        else:
            total += (n // 10**i) * (9 if i == 1 else 10)
    return total

if __name__ == "__main__":
    n = int(input())  # read input from stdin
    print(count_digit_one(n))  # print the result to stdout
