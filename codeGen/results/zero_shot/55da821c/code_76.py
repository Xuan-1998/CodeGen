import sys

def solve():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((s, x))

    plants.sort(key=lambda x: x[1])

    sections = [[] for _ in range(m)]
    for plant in plants:
        sections[plant[0] - 1].append(plant)

    replant_count = 0
    for section in sections:
        if len(section) > 1:
            replant_count += len(section) - 1

    print(replant_count)

if __name__ == "__main__":
    solve()
