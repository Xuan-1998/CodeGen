from math import sqrt

def dp(i, j):
    if i == 0 or j == 0:  # base case: edge of the rectangle
        return 0
    min_squares = float('inf')
    for k in range(i):  # iterate over previous cells
        for m in range(j):
            if (i-k) * (j-m) == int(sqrt((i-k)**2 + (j-m)**2))**2:  # check if (i-k)*(j-m) is a square number
                min_squares = min(min_squares, dp(k, m) + 1)
    return min_squares

def main():
    n, m = map(int, input().split())  # read input
    print(dp(n, m))  # print the result

if __name__ == "__main__":
    main()
