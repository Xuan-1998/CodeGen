m, n = map(int, input().split())  # read m and n from stdin
grid = [[int(x) for x in input().split()] for _ in range(m)]  # read grid from stdin

min_sum_path = min_sum(0, 0)  # initial call with top-left corner (0,0)

print(min_sum_path)  # print the minimum sum of all numbers along the path
