def find_winning_teams():
    n = int(input())  # Read input for number of phases

    dp = {}  # Initialize dynamic programming dictionary
    for s in (1 << i) for i in range(n+1):
        dp[(i, bin(s)[2:].zfill(n))] = []

    for i in range(n-1, -1, -1):  # Iterate over phases in reverse order
        for k in range(2**i):  # Iterate over possible skill levels for phase i
            s = (k << i) | ((1<<n)-1)^((1<<i)-1)
            if bin(s)[2:].zfill(n)[i] == '1':  # If team wins in this phase
                dp[(i, bin(s)[2:].zfill(n))] += [j for j in range(2**i) if (k ^ j) & ((1 << i) - 1)]

    winning_teams = []
    for s in (1 << i) for i in range(n+1):
        if dp[(n, bin(s)[2:].zfill(n))]:  # If any team has won at least one game
            winning_teams += [j for j in range(2**i) if all((s ^ (1 << j)) & ((1 << i) - 1) == 0 for i in range(n))]

    winning_teams.sort()  # Sort the winning teams in ascending order

    print(*winning_teams, sep='\n')  # Print the winning teams

find_winning_teams()
