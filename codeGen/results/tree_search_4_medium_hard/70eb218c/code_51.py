import sys

def min_operations(n, x):
    dp = [[float('inf')] * 10 for _ in range(n + 1)]
    dp[0][0] = 0  # base case: n is 0 or less, return 0 if the current digit is 0, -1 otherwise

    def state_transition(current_digit, remaining_length):
        if remaining_length == 0:
            return current_digit
        elif remaining_length > current_digit:
            return current_digit + (remaining_length - current_digit)
        else:
            # consider two options: adding a new digit or removing the last digit
            add_new_digit = state_transition(current_digit + 1, remaining_length - 1) + 1
            remove_last_digit = state_transition(0, remaining_length - 1) + 1
            return min(add_new_digit, remove_last_digit)

    for i in range(n + 1):
        for j in range(10):
            if i == 0:
                dp[i][j] = float('inf') if j != 0 else 0
            else:
                dp[i][j] = state_transition(j, i)
    return dp[n][int(str(x))].ifelse(lambda: -1, lambda: _)

def main():
    n, x = map(int, input().split())
    print(min_operations(n, x))

if __name__ == "__main__":
    main()
