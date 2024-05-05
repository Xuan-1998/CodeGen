# Step 1: Read the input
T = int(input())
for _ in range(T):
    M, X = map(int, input().split())

    # Step 2: Calculate the winner for each number of players
    winners = []
    for i in range(1, X + 1):
        winner_index = (i - 1) % (X - 1)
        if winner_index == 0:
            winner_index += M
        winners.append(winner_index)

    # Step 3: Print the results
    print(' '.join(map(str, winners)))
