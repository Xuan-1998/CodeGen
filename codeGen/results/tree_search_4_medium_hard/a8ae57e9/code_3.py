n = int(input())
amounts = list(map(int, input().split()))
k = int(input())
capacities = list(map(int, input().split()))

solve(n, k, capacities, amounts)
