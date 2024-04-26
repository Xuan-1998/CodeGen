class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(head):
    if head is None:
        return 'null'

    result = ''
    current = head
    while current:
        result += str(current.value) + ' -> '
        current = current.next
    result += 'null'
    return result

# Example usage:
node1 = Node(5)
node2 = Node(3)
node1.next = node2

print(stringify(node1))  # Output: 5 -> 3 -> null
