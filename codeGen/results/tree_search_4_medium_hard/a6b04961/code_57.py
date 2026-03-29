def solve():
    n, m = map(int, input().split())
    memo = {}
    
    def dp(tail_length, last_node_in_tail):
        if (tail_length, last_node_in_tail) in memo:
            return memo[(tail_length, last_node_in_tail)]
        
        beauty = 0
        for i in range(m):
            u, v = map(int, input().split())
            
            if u == tail_length + 1 and v != last_node_in_tail:
                beauty = (tail_length + 1) * (spine_count + 1)
                break
            elif v == tail_length + 1 and u != last_node_in_tail:
                beauty = (tail_length + 1) * (spine_count + 1)
                break
        
        memo[(tail_length, last_node_in_tail)] = beauty
        return beauty
    
    max_beauty = 0
    for i in range(1, n):
        max_beauty = max(max_beauty, dp(i, 0))
    
    print(max_beauty)

if __name__ == "__main__":
    solve()
