from sys import stdin

def can_reach_last_index(arr):
    last_index = len(arr) - 1
    max_reachable = 0
    
    for i in range(len(arr)):
        if i > max_reachable:
            return False
        
        max_reachable = max(max_reachable, i + arr[i])
    
    return True

if __name__ == "__main__":
    n = int(stdin.readline().strip())
    arr = [int(x) for x in stdin.readline().split()]
    
    if can_reach_last_index(arr):
        print("YES")
    else:
        print("NO")
