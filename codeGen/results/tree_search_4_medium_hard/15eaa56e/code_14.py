import sys

def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    
    def is_sorted_column(j):
        return all(table[i][j] <= table[i+1][j] if i < n-1 else True for i in range(n))
    
    print("Yes" if any(is_sorted_column(j) for j in range(m)) else "No")

if __name__ == "__main__":
    main()
