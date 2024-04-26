from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(head):
    result = ""
    queue = deque([head])

    while queue:
        node = queue.popleft()
        if node:
            result += str(node.value) + " -> "
            queue.append(node.next)
        else:
            result += "null"
            break

    return result.rstrip()  # remove trailing arrow and space

# Example usage
node1 = Node(5)
node2 = Node(6)
node3 = Node(7)

node1.next = node2
node2.next = node3

print(stringify(node1))  # Output: "5 -> 6 -> 7 -> null"
