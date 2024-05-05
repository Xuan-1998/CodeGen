import math

def findCount(n):
    count = 0
    for i in range(1, int(math.log2(n)) + 1):
        # Count the number of ones that can be appended to (i-1)-digit numbers
        count += 10 ** (n - i) * i
    return count

if __name__ == "__main__":
    n = int(input())
    print(findCount(n))
