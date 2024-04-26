from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(head):
    queue = deque()
    node = head
    
    while node:
        queue.append(str(node.value))
        node = node.next
    
    result = ' -> '.join(queue) + 'null'
    
    return result

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(stringify(head))  # Output: "1 -> 2 -> 3null"
