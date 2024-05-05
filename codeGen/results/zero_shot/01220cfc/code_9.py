from sys import stdin, stdout

def solution(arr):
    n = len(arr)
    last_index = n - 1
    curr_index = 0
    
    while curr_index < last_index:
        next_index = curr_index + arr[curr_index]
        
        if next_index > last_index or next_index < 0:
            return False
        
        curr_index = next_index
        
    return True

arr = list(map(int, stdin.readline().split()))
stdout.write(str(solution(arr)))
