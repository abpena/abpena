import math
from Node import Node


class LRC:
    def __init__(self, maxc):
        self.dictionary = {}
        self.count = 0
        self.length = maxc
        self.head = None
        self.tail = None

    def put(self, letter, value):
        current = Node(letter, value)
        if self.head is None:
            self.head = current # adding one thing to the list
            self.tail = current
            self.dictionary[letter] = current # making the dictionary
            self.count += 1
        elif self.count < self.length:
            self.tail.next = current
            current.previous = self.tail
            self.tail = current
            self.dictionary[letter] = current # adding everything to the dictionary the right way
            self.count += 1
        else:
            self.head = self.head.next
            self.head.previous = None
            self.tail.next = current
            current.previous = self.tail
            self.tail = current
            self.dictionary[letter] = current  # adding everything to the dictionary the right way

    def get(self, key):
        temp = -1
        if key in self.dictionary:
            temp = self.dictionary[key]
            if temp == self.tail or len(self.dictionary) == 1:
                return
            elif temp == self.head:
                self.head = self.head.next
                self.head.previous = None
                self.tail.next = temp
                temp.previous = self.tail
                self.tail = temp
            else:
                left_node = temp.previous
                right_node = temp.next
                left_node.next = right_node
                right_node.previous = left_node
                self.tail.next = temp # adding to the end
                temp.previous = self.tail
                self.tail = temp
        return temp.value # returning the value

    def size(self):
        if self.dictionary is not None:
            return self.count

    def max_capacity(self):
        return self.length
