def min_mana_required():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # number of monsters
        k_values = list(map(int, input().split()))  # appearance times
        h_values = list(map(int, input().split()))  # health values

        min_mana = float('inf')
        current_mana = 0
        for i in range(n):
            while k_values[i] > current_mana:
                current_mana += 1
            min_mana = min(min_mana, h_values[i] + (current_mana - k_values[i]))

        print(min_mana)

min_mana_required()
