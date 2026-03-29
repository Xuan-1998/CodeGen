def countOnes(n):
    totalOnes = 0
    for i in range(n+1):
        ones = bin(i).count('1')
        totalOnes += ones
    return totalOnes

n = int(input())
print(countOnes(n))
