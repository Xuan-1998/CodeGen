import sys

def check_sorted(table):
    n = len(table)
    m = len(table[0])
    
    for i in range(n):
        max_val = table[i][0]
        
        for j in range(m-1):
            if table[i][j] > table[i][j+1]:
                return False
            max_val = max(max_val, table[i][j+1])
            
        if max_val < table[i][m-1]:
            return False
    
    return True

def solve():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    
    k = int(input())
    
    for _ in range(k):
        l, r = map(int, input().split())
        
        is_sorted = True
        max_val = 0
        
        for j in range(m):
            max_col = max(table[l-1][j], table[r][j])
            
            if not check_sorted([[table[i][j] for i in range(l-1, r+1)]]):
                is_sorted = False
                break
            max_val = max(max_val, max_col)
        
        if is_sorted:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()
