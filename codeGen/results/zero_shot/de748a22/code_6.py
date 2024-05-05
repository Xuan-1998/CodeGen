import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    signs = list(sys.stdin.readline().strip())

    # Preprocess the array to store the cumulative sum of the signs
    cum_signs = [0] * (n + 1)
    for i in range(n):
        cum_signs[i + 1] = cum_signs[i] + (1 if signs[i] == '+' else -1)

    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        # Calculate the sign-variable sum for the given range
        sum_signs = cum_signs[r] - cum_signs[l]
        # Find the minimal number of elements that can be removed to make the sum zero
        min_remove = abs(sum_signs) // 2
        print(min_remove)

if __name__ == "__main__":
    solve()
