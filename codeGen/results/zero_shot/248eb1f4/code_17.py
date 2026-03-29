def winner_game():
    T = int(input())
    
    for _ in range(T):
        M, X = map(int, input().split())
        
        winners = [0] * (X + 1)
        
        for i in range(2, X + 1):
            winners[i] = (winners[i - 1] + M) % i
            
        print(*winners[1:], sep='\n')
