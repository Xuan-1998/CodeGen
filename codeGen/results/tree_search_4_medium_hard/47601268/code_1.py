import sys

def findCount(n):
    dp = [True] * (n.bit_length() + 1)

    for k in range(1, n.bit_length() + 1):
        for num in range(2 ** k):
            if bin(num)[2:].zfill(k).count('1') > 1:
                dp[k] = False
                break

    return sum(dp)


if __name__ == "__main__":
    n = int(input())
    print(findCount(n))
