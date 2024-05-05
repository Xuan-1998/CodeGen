def count_non_negative_integers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(input())  # read input from stdin
print(count_non_negative_integers_without_consecutive_ones(n))  # print output to stdout
