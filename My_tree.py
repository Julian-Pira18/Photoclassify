from My_queue import *


class Node_Tree():
    def __init__(self, data):
        self.data = data
        self.left = self.rigth = None


class Tree:
    def __init__(self):
        self.root = None
        self.size = None

    def insert(self, data):
        node = Node_Tree(data)
        ref = self.root

        if ref == None:
            self.root = node
            return

        while True:
            if ref.data.data == node.data.data:
                break

            elif ref.data.data > node.data.data:
                if ref.left:
                    ref = ref.left

                else:
                    ref.left = node
                    break

            else:
                if ref.rigth:
                    ref = ref.rigth

                else:
                    ref.rigth = node
                    break

    def show(self, number=None):
        ref = self.root
        if ref is None:
            return

        queue = Queue()
        queue.enqueue(ref)

        if number == None:
            while queue:
                if queue.first == None:
                    break
                node = queue.dequeue()
                print(node.data.data, end=" ")

                if node.left:
                    queue.enqueue(node.left)
                if node.rigth:
                    queue.enqueue(node.rigth)
        else:
            for _ in range(number):
                if queue.first == None:
                    break
                node = queue.dequeue()
                print(node.data.data, end=" ")

                if node.left:
                    queue.enqueue(node.left)
                if node.rigth:
                    queue.enqueue(node.rigth)

    def search(self, data):
        ref = self.root

        while ref:
            if ref.data.data == data:
                print(ref.data.data)
                return True

            elif ref.data.data > data:
                ref = ref.left

            else:
                ref = ref.rigth

        return False
