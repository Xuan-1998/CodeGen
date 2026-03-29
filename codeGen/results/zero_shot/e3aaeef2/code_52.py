t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = str(n)
    for _ in range(m):
        temp = ""
        for digit in result:
            if digit == '9':
                temp += '1'
            else:
                temp += str(int(digit) + 1)
        result = temp
    print(len(result) % (10**9 + 7))
