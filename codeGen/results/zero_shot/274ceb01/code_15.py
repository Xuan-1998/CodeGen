def min_sum_below_water(n, m):
    total_marks = 0
    min_sum = float('inf')
    for i in range(1, n+1):
        total_marks += i - m[i-1]
        if total_marks < min_sum:
            min_sum = total_marks
    return min_sum

if __name__ == "__main__":
    n = int(input())  # read the number of days from stdin
    m = list(map(int, input().split()))  # read the marks above water level on each day
    print(min_sum_below_water(n, m))  # call the function and print the result
