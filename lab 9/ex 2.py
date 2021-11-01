'''
Реализуйте класс BinTree двоичного дерева, итерирование по которму происходит в порядке обхода в глубину.
'''

class Node:
    def __init__(self, data, left = None , right = None):
        self.data = data
        self.left = left
        self.right = right

class BinTree:
    def __init__(self,tree):
        self.work_queue = [tree]
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.work_queue) > 0:
            subtree = self.work_queue.pop()
            if subtree.right is not None:
                self.work_queue.append(subtree.right)
            if subtree.left is not None:
                self.work_queue.append(subtree.left)
            return subtree.data
        else:
            raise StopIteration
T = Node(2,Node(7,Node(4,Node(9),Node(45)),Node(6,Node(17))),Node(18,Node(15),Node(3)))
#               2
#          7        18
#     4     6    15  3
#   9 45  17
tree = BinTree(T)
for i in tree:
    print(i)