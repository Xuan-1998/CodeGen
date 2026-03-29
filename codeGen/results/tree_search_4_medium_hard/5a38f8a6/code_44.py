import math

def min_perfect_squares(n):
    dp = {0: 0}  # Initialize dictionary with base case
    for i in range(1, n + 1):
        if i ** 0.5 == int(i ** 0.5):  # Check if i is a perfect square
            dp[i] = 1
        else:
            min_count = float('inf')
            for j in range(int(math.sqrt(i)), -1, -1):
                if j ** 2 <= i:
                    count = dp.get(j ** 2, float('inf')) + 1
                    if count < min_count:
                        min_count = count
            dp[i] = min_count

    return dp[n]

def main():
    n = int(input())  # Read input from stdin
    print(min_perfect_squares(n))  # Print the result to stdout

if __name__ == "__main__":
    main()
