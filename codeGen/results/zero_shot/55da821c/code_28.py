code
n, m = map(int, input().split())
sections = [[] for _ in range(m)]
replantings = 0

for _ in range(n):
    species, x = map(int, input().split())
    section = (species - 1) % m  # wrap around if necessary
    if sections[section]:
        replantings += 1
    sections[section].append(x)

print(replantings)
