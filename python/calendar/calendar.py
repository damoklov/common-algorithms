class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class Calendar:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        nodes = list()
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes)

    def insert_into_sorted(self, node_to_insert):
        if self.head is None:
            node_to_insert.next = self.head
            self.head = node_to_insert
        elif self.head.data[0] > node_to_insert.data[0]:
            node_to_insert.next = self.head
            self.head = node_to_insert
        else:
            current = self.head
            while current.next is not None and current.next.data[0] < node_to_insert.data[0]:
                current = current.next
            if current.next is not None and current.next.data[0] == node_to_insert.data[0]:
                if current.next.data[1] < node_to_insert.data[1]:
                    current = current.next
                    node_to_insert.next = current.next
                    current.next = node_to_insert
                else:
                    node_to_insert.next = current.next
                    current.next = node_to_insert
            else:
                node_to_insert.next = current.next
                current.next = node_to_insert

    def optimize(self):
        current = self.head
        while current.next is not None:
            if current.data[1] >= current.next.data[0]:
                current.data = (current.data[0], max(current.next.data[1], current.data[1]))
                current.next = current.next.next
            else:
                current = current.next
