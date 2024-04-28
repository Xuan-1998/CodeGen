def winning_teams(state):
    n = len(state)
    winners = []
    
    # Base case: only one team left, it wins
    if n == 1:
        return [state[0]]
    
    # Find the winner of the current game (i.e., the first bit in the state)
    winner = '1' if state[0] == '1' else '0'
    
    # Recursively find the winning teams for the remaining games
    winners += winning_teams(state[1:])  # Remove the first team from consideration
    
    # If the current team wins, add it to the list of winners
    if winner == state[0]:
        winners.append(state)
    
    return winners

def main():
    n = int(input())
    state = input().strip()
    
    winning_teams_list = winning_teams(list(state))
    print("\n".join(sorted(map(str, winning_teams_list))))

if __name__ == "__main__":
    main()
