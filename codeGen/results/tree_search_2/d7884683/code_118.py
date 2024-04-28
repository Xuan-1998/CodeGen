from sys import stdin

def solve():
    t = int(stdin.readline())
    dp = {0: 1}

    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        
        res = 1
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(n):
            if left_sum == total_sum - left_sum:
                res += 1
            left_sum += arr[i]
            
        print(res)

solve()
