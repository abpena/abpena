import math
from HeapNode import HeapNode


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def insert(self, word):
        for i in range(len(self.tree)):
            if word == self.tree[i].word:
                self.tree[i].occur += 1
                self._percolate_up(i)
                return

        node = HeapNode(word)
        self.insert_helper(node)

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert_helper(self, node):
        self.tree.append(node)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index].occur < self.tree[i].occur:
            # print(self.tree[parent_index].word + " " + self.tree[i].word)
            # print(str(self.tree[parent_index].occur) + " " + str(self.tree[i].occur))
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)
        elif self.tree[parent_index].occur == self.tree[i].occur and self.tree[parent_index].word < self.tree[i].word:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)
