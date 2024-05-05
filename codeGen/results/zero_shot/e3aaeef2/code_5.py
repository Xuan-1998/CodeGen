def next_digit(n):
    n = str(n)
    result = ''
    for d in n:
        new_d = str(int(d) + 1).zfill(1)  # convert int to string and zero-pad if necessary
        result += new_d
    return int(result)

t = int(input())  # read t from stdin
for _ in range(t):
    n, m = map(int, input().split())  # read n and m from stdin
    n = next_digit(n)
    m -= 1  # subtract 1 from m since we've already applied one operation
    while m > 0:
        n = next_digit(n)
        m -= 1

    result = len(str(n)) % (10**9 + 7)  # calculate the length of the resulting number modulo 10^9+7
    print(result)
