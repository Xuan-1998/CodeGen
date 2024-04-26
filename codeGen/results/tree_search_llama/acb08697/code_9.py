n = int(input())
operations = input().split()
additions = operations.count('+')
removals = len(operations) - additions

print(min(additions, 0))
