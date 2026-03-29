code
values = {}
def dfs(vertex, parent):
    if parent != -1:
        values[parent] = min(values.get(parent, 0), values.get(vertex, 0))
    if vertex < n:
        dfs(p[vertex], vertex)

def update_value(vertex):
    values[vertex] += min(0, values.get(vertex, 0) - l[vertex]) + r[vertex]

def calculate_min_operations():
    min_operations = 0
    for vertex in range(1, n):
        if p[vertex] != -1:
            update_value(p[vertex])
        min_operations += values.get(vertex, 0)
    return min_operations

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = [0] + list(map(int, input().split()))
        l = list(map(int, [input().split() for _ in range(n-1)]))
        r = list(map(int, [input().split() for _ in range(n-1)]))
        dfs(1, -1)
        print(calculate_min_operations())
