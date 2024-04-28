def is_subset_sum_divisible_by_m(n, m):
    prefix_sums = [0]  # Initialize a list to store prefix sums

    for i in range(n):
        current_num = int(input())  # Read the ith number from input
        new_sum = prefix_sums[-1] + current_num  # Calculate the new sum
        prefix_sums.append(new_sum % m)  # Store the new sum modulo m

    return 0 if any(prefix_sums[i:] for i in range(n)) else 1


n, m = map(int, input().split())  # Read n and m from input
print(is_subset_sum_divisible_by_m(n, m))
