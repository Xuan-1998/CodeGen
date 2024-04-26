MOD = 998244353

def add_mod(a, b, mod):
    return (a + b) % mod

def sub_mod(a, b, mod):
    return (a - b + mod) % mod

def mul_mod(a, b, mod):
    return (a * b) % mod

def calculate_f(A, n):
    # Initialize dp array with -1, representing uncalculated states
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def f(subseq_len, last_taken, taken_count):
        if dp[subseq_len][taken_count] != -1:
            return dp[subseq_len][taken_count]

        if subseq_len == 0:
            return 0 if taken_count == 0 else A[last_taken - 1]

        # Case 1: Do not take the current element
        total = f(subseq_len - 1, last_taken, taken_count)

        if A[subseq_len - 1] >= 0:
            # Case 2: Take the current element if it is positive
            if taken_count > 0:
                total = add_mod(total, mul_mod(f(subseq_len - 1, last_taken, taken_count - 1), taken_count, MOD), MOD)
            total = add_mod(total, f(subseq_len - 1, subseq_len, taken_count + 1), MOD)
        else:
            # Case 3: Consider the current element if it is negative
            if taken_count > 0:
                total = add_mod(total, f(subseq_len - 1, last_taken, taken_count - 1), MOD)

        dp[subseq_len][taken_count] = total
        return total

    # Sum up f(B) for all subsequences B
    result = 0
    for subseq_len in range(1, n + 1):
        for last_taken in range(1, subseq_len + 1):
            result = add_mod(result, f(subseq_len, last_taken, 1), MOD)

    return result

def main():
    n = int(input().strip())
    A = []
    for _ in range(n):
        line = input().strip().split()
        if line[0] == '+':
            A.append(int(line[1]))
        else:
            A.append(-1)
    print(calculate_f(A, n))

if __name__ == "__main__":
    main()
