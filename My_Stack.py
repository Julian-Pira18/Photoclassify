

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, data):

        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
            self.bottom = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
                self.bottom = None
            return data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def show(self, number=None):
        ref = self.top
        if number:
            for _ in range(number):
                print(ref.data, end=" ")
                ref = ref.next
        else:
            while ref:
                print(ref.data, end=" ")
                ref = ref.next

    def search(self, number, update=None):

        ref = self.top
        while ref:
            if ref.data == number:
                ref.data = update
                break
            ref = ref.next
