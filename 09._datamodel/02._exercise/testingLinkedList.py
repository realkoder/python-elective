from linkedlist import LinkedList
from node import Node

myLinkedList = LinkedList()
node = Node("Test")

print(f'This is size when instantiated {len(myLinkedList)}')
myLinkedList.append(node)

print(f'This is size after append {len(myLinkedList)}')

print(f'Data at index 0: {myLinkedList[0].data}')

print("----------------------------------------")

new_node = Node("NYTNYTNYT")
myLinkedList.append(new_node)

print(f'This is size after append {len(myLinkedList)}')

print(f'Data at index 1: {myLinkedList[-1].data}')