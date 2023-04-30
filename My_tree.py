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
            if ref.data == node.data:
                break

            elif ref.data > node.data:
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

    def search(self, data):
        ref = self.root

        while ref:
            if ref.data == data:
                print(f"ref= {ref.data}  data={data}")
                return True

            elif ref.data > data:
                ref = ref.left

            else:
                ref = ref.rigth
        return False
