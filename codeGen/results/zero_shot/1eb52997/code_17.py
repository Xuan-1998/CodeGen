import sys
from collections import deque

def main():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        grid = []
        
        for _ in range(N):
            row = list(sys.stdin.readline().strip())
            grid.append(row)
            
        count = 0
        
        for i in range(N):
            for j in range(N - 1, -1, -1):  
                if grid[i][j] == '.':
                    can_place_mirror = True
                    
                    for k in range(j + 1, N):
                        if grid[i][k] == '#':
                            can_place_mirror = False
                            break
                    
                    if can_place_mirror:
                        count += 1
        
        print(count)

if __name__ == "__main__":
    main()
