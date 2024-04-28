n = int(input())
operations = input()

init_stones = 0 if len([s for s in operations if s == '+']) % 2 else 1

print(min(max(0, init_stones + sum(1 if s == '+' else -1 for s in operations)), n))
