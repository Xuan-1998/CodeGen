import sys
T = int(input())  # read T, the number of test cases
for _ in range(T):
    M, X = map(int, input().split())  # read M and X for each test case
    winners = [0] * (X + 1)  # initialize an array to store the winner indices
    
    # calculate the winner index for each number of players from 1 to X
    for i in range(1, X + 1):
        winner_index = ((M - 1) * i) % i  # calculate the winner index based on M and i
        winners[i] = winner_index + 1  # store the winner index in the array
    
    print(*winners[1:])  # print the winner indices for each number of players from 1 to X
