import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = {(i, (0, 0)): 0.0}
        for i in range(n):
            count1, num1, num2 = map(int, input().split())
            P_i = count1 / (count1 + count2)
            for k in range(count1+1):
                dp[(i, (k, count2-k))] = max(
                    P_i * (1 if i == 0 else dp.get((i-1, (k-1, count2-k)), 0)) + 
                    (1 - P_i) * (1 if k > 0 else dp.get((i-1, (count1-1, count2)), 0)),
                    (1 - P_i) * (1 if i == 0 or k < count1 else dp.get((i-1, (k, count2-k-1)), 0)) + 
                    P_i * (1 if i == 0 or k > 0 else dp.get((i-1, (count1-1, count2-1)), 0))
                )
        print(round(dp.get((n, (count1-count1//2, count2-count2//2)), 0), 6))

if __name__ == "__main__":
    solve()
