def countOnes(n):
    memo = {0: 1}  # base case for i=0
    total Ones = 0

    for i in range(1, n + 1):
        if i == 1:
            totalOnes += 1
        elif i % 2 == 0:
            totalOnes += memo[i // 2]
        else:
            totalOnes += memo[(i - 1) // 2] + (1 if i % 2 == 1 else 0)

    return totalOnes

n = int(input())
print(countOnes(n))
