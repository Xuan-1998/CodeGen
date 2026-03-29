from pulp import LpMaximize, LpProblem, lpSum

def max_profit():
    # Read input data from stdin
    n, m, c0, d0 = map(int, input().split())
    ai, bi, ci, di = [], [], [], []
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        ai.append(a)
        bi.append(b)
        ci.append(c)
        di.append(d)

    # Create the LP problem
    prob = LpProblem("BunProfit", LpMaximize)

    # Decision variables
    x = [(i,) for i in range(m)]
    y = [0]

    # Objective function
    profit = lpSum(x + y, lambda v: di[i] * v - (ai[i] + bi[i]) * ci[i])

    # Constraints
    prob += lpSum(x) <= n  # Total dough used ≤ available dough
    for i in range(m):
        prob += ai[i] * x[i] <= ai[i]  # Total stuffing used ≤ available quantity
    prob += c0 * y[0] <= c0  # Dough used without stuffing ≤ available dough

    # Solve the LP problem
    prob.solve()

    # Print the maximum profit
    print(int(value(prob.objective)))

if __name__ == "__main__":
    max_profit()
