def min_sum_of_product(a):
    n = len(a)
    dp_dict = {}

    def dp(i, s):
        if (i, s) in dp_dict:
            return dp_dict[(i, s)]
        
        if i == n:
            return 0
        
        if s - a[i] < 0:
            result = dp(i + 1, s)
        elif s >= a[i]:
            result = min(dp(i + 1, s - a[i]), dp(i + 1, s))
        else:
            raise ValueError("Invalid input")
        
        dp_dict[(i, s)] = result
        return result

    total_sum = sum(a)
    return min([dp(1, total_sum - j) for j in range(total_sum + 1)])

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_sum_of_product(a))
