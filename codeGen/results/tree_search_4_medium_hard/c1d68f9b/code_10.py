def polygon_configuration():
    n = int(input())
    moods = list(map(int, input().split()))
    
    max_length = 0
    states = {0: 0}
    
    for i in range(n):
        if moods[i] == 1:
            if max_length % 2 == 0:
                max_length += 2
            else:
                max_length = 0
        else:
            max_length = 0
        
        states[max_length] = i + 1
    
    if max_length >= 3:
        print("YES")
    else:
        print("NO")

polygon_configuration()
