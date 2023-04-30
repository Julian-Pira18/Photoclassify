class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):

        node = Node(data)

        if self.last:
            self .last.next = node
            self.last = node
        else:
            self.first = node
            self.last = node

        self.size += 1

    def dequeue(self):
        if self.first:
            data = self.first.data
            self.size -= 1

            if self.first.next:
                self.first = self.first.next
            else:
                self.first = None
                self.last = None
            return data

    def peek(self):
        if self.first:
            print(self.first.data)
        else:
            return None


my_Queue = Queue()
my_Queue.enqueue(4)
my_Queue.enqueue(5)
my_Queue.enqueue(9)
my_Queue.enqueue(3)
my_Queue.enqueue(8)
my_Queue.dequeue()
my_Queue.dequeue()
my_Queue.dequeue()
my_Queue.peek()
print(my_Queue.size)
