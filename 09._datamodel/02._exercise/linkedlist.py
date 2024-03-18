from node import Node

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.amount = 0

    def __len__(self):
        return self.amount
    
    def append(self, node):
        current_node = self.head   

        if current_node is None:
            self.head = node
            self.amount += 1
            return None     

        while current_node is not None:      
            if current_node.next is None:
                current_node.next = node
                self.amount += 1
                return None

            current_node = current_node.next
        
    # First approach to getitem
    # def __getitem__(self, index):
    #     if self.head is None:
    #         return 0

    #     current_node = self.head
    #     current_index = 0

    #     while current_node is not None:
    #         if current_index == index:
    #             print("HEYHYE")
    #             print(current_index)
    #             return current_node

    #         current_index += 1
    #         current_node = current_node.next

    # Second approach to getitem
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._get_node_by_index(key)

        elif isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else len(self)
            step = key.step if key.step is not None else 1
            
            if start < 0:
                start = len(self) + start
            if stop < 0:
                stop = len(self) + stop

            sliced_list = LinkedList()
            current_index = 0
            current_node = self.head
            
            while current_node is not None and current_index < stop:
                if current_index >= start and (current_index - start) % step == 0:
                    sliced_list.append(current_node)
                current_node = current_node.next
                current_index += 1
            
            return sliced_list

    def _get_node_by_index(self, index):
        current_index = 0
        current_node = self.head

        while current_node is not None:
            if current_index == index:
                return current_node

            current_index += 1
            current_node = current_node.next

        raise IndexError("Index out of range")

