import sys

def solve():
    a, b = map(int, input().split())
    
    dp = {}
    total_sum = 0
    
    for i in range(315):
        if (a, b, i) not in dp:
            if i == 0:
                dp[(a, b, i)] = a ^ b
            else:
                left_shifted_b = b << 1
                dp[(a, b, i)] = dp.get((a, b, i - 1), 0) + (a ^ left_shifted_b)
        total_sum += dp[(a, b, i)]
    
    print(total_sum % (10**9 + 7))

if __name__ == "__main__":
    solve()
