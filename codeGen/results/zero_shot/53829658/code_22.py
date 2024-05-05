codeblock
def main():
    n = int(input())
    roofs = []
    for _ in range(n-1):
        si, ti = map(int, input().split())
        roofs.append((si, ti))
    
    root_node = find_root_node(roofs)
    min_reversals_count = min_reversals(root_node, roofs)
    
    print(min_reversals_count)
    for node in range(1, n):
        if node != root_node:
            print(node)

main()
