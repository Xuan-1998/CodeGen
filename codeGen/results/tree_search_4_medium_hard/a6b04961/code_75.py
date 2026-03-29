from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    memo = defaultdict(int)

    def dp(tail_length, number_of_spines):
        if (tail_length, number_of_spines) in memo:
            return memo[(tail_length, number_of_spines)]
        
        max_beauty = 0
        for _ in range(n - tail_length):  # Explore all possible extensions of the current tail
            new_beauty = dp(tail_length + 1, number_of_spines + 1) * (n - tail_length)
            if new_beauty > max_beauty:
                max_beauty = new_beauty
        
        memo[(tail_length, number_of_spines)] = max_beauty
        return max_beauty
    
    max_beauty = 0
    for _ in range(n):  # Traverse all vertices as potential starting points
        max_beauty = max(max_beauty, dp(1, 0) * (n - 1))
    
    print(max_beauty)

if __name__ == "__main__":
    solve()
