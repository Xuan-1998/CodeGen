n = int(input())  # read the input value n
p_values = [int(x) for x in input().split()]  # read the p_i values

dp_moves = dp(n + 1)
print(dp_moves % 1000000007)  # print the answer modulo 10^9 + 7
