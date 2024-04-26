def find_matches():
    n = int(input())
    arr = list(map(int, input().split()))
    
    matches = set()
    
    for i in range(1, n + 1):
        if i == arr[i - 1]:
            matches.add(i)
            
    print(list(matches))

find_matches()
