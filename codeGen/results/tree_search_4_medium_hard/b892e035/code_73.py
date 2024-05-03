import sys

def solve():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        
        dp = {(0, 0): 1.0}
        
        for i in range(1, n + 1):
            count1, count2 = map(int, input().split())
            
            if (i - 1, count1) not in dp:
                dp[(i - 1, count1)] = (dp.get((i - 1, count1), 0.0) + dp.get((i - 1, count2), 0.0)) * 0.5
            
            if (i - 1, count2) not in dp:
                dp[(i - 1, count2)] = (dp.get((i - 1, count1), 0.0) + dp.get((i - 1, count2), 0.0)) * 0.5
            
            if i > 1 and (i - 2, count1) in dp:
                for k in range(count1):
                    dp[(i, k, count1 - k)] = dp[(i - 1, count1 - k, count2)] * dp.get((i - 1, count1), 0.5)
                
            if i > 1 and (i - 2, count2) in dp:
                for k in range(count2):
                    dp[(i, count1, count2 - k)] = dp[(i - 1, count1, count2 - k)] * dp.get((i - 1, count2), 0.5)
            
            print(round(dp.get((n, 0, 0), 0.0) + dp.get((n, 0, 1), 0.0) - 1.0, 6))

if __name__ == "__main__":
    solve()
