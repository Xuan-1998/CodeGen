from bisect import bisect_left

MOD = 998244353

def main():
    n = int(input().strip())
    A = [input().strip().split() for _ in range(n)]
    
    pos_elements = []
    total_sum = 0

    for i in range(n):
        operation, x = A[i]
        if operation == '+':
            x = int(x)
            # Count the number of subsequences in which x will be included and not removed
            num_smaller = bisect_left(pos_elements, x)
            num_larger_or_equal = len(pos_elements) - num_smaller
            num_subseq = pow(2, num_smaller) * pow(2, n - i - 1)
            contribution = x * num_subseq % MOD
            total_sum = (total_sum + contribution) % MOD
            pos_elements.append(x)
            pos_elements.sort()
        else:
            # For '-', just remove the last element if the list is not empty
            if pos_elements:
                pos_elements.pop()

    print(total_sum)

if __name__ == "__main__":
    main()
