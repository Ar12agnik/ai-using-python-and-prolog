import numpy as np
import math

class Tree:
    def __init__(self, n: int) -> None:
        self.tree = np.zeros(n, dtype='int64')
        self.last = -1

    def insert(self, data: int):
        self.last += 1
        if self.last >= len(self.tree):
            print("Can't insert more values!!")
            return
        self.tree[self.last] = data
    def print_tree(self):
        # Print the tree level by level
        level = 0
        index = 0
        while index <= self.last:
            nodes_in_level = 2 ** level  # Number of nodes in the current level
            # Print all nodes in the current level
            for _ in range(nodes_in_level):
                if index <= self.last:  # Check to avoid index out of range
                    print(self.tree[index], end=' ')
                    index += 1
            print()  # Newline for the next level
            level += 1  # Move to the next level  # Number of nodes in the next level
    def bfs(self,target:int):
        found=False
        for i in range(self.last+1):
            if self.tree[i] == target:
                index=i
                found=True
                break
        if not found:
            print("element doesnot exist")
            return
        level = math.floor(math.log2(index+1))
        return level
tree = Tree(15)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
print(f'Element found at level: {tree.bfs(5)}')
tree.print_tree()