class Node(object):
    item = ""
    #  Height = 0
    height = 0

    def __init__(self, item):
        self.item = item
        self.parent = None
        self.right = None
        self.left = None
        self.color = ""


class avl:
    count = 0
    root = None

    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def get_height(root):
        # c = avl()
        value_h = root.get_tree_height(root)
        return value_h

    @staticmethod
    def get_tree_height(root):
        if root is None:
            return 0
        l_h = root.get_tree_height(root.left)
        r_h = root.get_tree_height(root.right)
        if l_h > r_h:
            return l_h + 1
        else:
            return r_h + 1

    @staticmethod
    def avl_tree_height(node_data):
        left_h = -1
        if node_data is not None:
            left_h = node_data.height
        right_h = -1
        if node_data.right is not None:
            right_h = node_data.right.height
        node_data.height = max(left_h, right_h) + 1

    def avl_tree_re_balance(self, node_data):
        self.avl_tree_height(node_data)
        if self.avl_tree_height(node_data) == -2:
            self.avl_tree_rotate_right(node_data.right)
            return self.avl_tree_rotate_left(node_data)

    @staticmethod
    def avl_tree_set_child(self, parent, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def avl_tree_replace_child(parent, current_child, new_child):
        c = avl()
        if parent.left is current_child:
            return c.avl_tree_set_child(parent, "left", new_child)
        elif parent.right is current_child:
            return c.avl_tree_set_child(parent, "right", new_child)
        return False

    def avl_tree_rotation_right(self, node_d):
        new_root = node_d.left
        temp = new_root.right

        new_root.right = node_d
        node_d.left = temp

        node_d.height = 1 + max(self.get_height(node_d.left), self.get_height(node_d.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def avl_rotate_left(self, node):
        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def insert_item(self, data):
        new_item = Node(data)
        if self.root is None:
            self.root = new_item
            self.root.left = None
            self.root.right = None
            new_item.height = new_item.height + 1
            return

        new_item.height = new_item.height + 1
        current_node = self.root
        while current_node is not None:
            if new_item.item < current_node.item:
                if current_node.left is None:
                    current_node.left = new_item
                    new_item.parent = current_node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_item
                    new_item.parent = current_node
                    current_node = None
                else:
                    current_node = current_node.right
        new_item = new_item.parent
        while new_item is not None:
            self.avl_tree_re_balance(new_item)
            new_item = new_item.parent
        #  return self.root

    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print(node.item)
        self.print_tree(node.right)


class RBTree:
    root = None
    # count = 0
    height = 0

    def __init__(self, root=None):
        self.root = root
        self.color = "black"

    @staticmethod
    def rbt_tree_update_height(node_data):
        left_h = -1
        if node_data is not None:
            left_h = node_data.height
        right_h = -1
        if node_data.right is not None:
            right_h = node_data.right.height
        node_data.height = max(left_h, right_h) + 1

    @staticmethod
    def rbt_tree_set_child(self, parent, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def rbt_tree_replace_child(parent, current_child, new_child):
        c = avl()
        if parent.left is current_child:
            return c.avl_tree_set_child(parent, "left", new_child)
        elif parent.right is current_child:
            return c.avl_tree_set_child(parent, "right", new_child)
        return False

    def rbt_tree_rotate_left(self, node_data):
        right_l_child = node_data.right.left
        if node_data.parent is None:
            self.rbt_tree_replace_child(node_data.parent, node_data, node_data.right)
        else:
            self.root = node_data
            self.root.parent = None
        self.rbt_tree_set_child(node_data.right, "left", node_data)
        self.rbt_tree_set_child(node_data, "right", right_l_child)

    def rbt_tree_rotate_right(self, node_data):
        left_r_child = node_data.left.right
        if node_data.parent is not None:
            self.rbt_tree_replace_child(node_data.parent, node_data, node_data.right)
        else:
            self.root = node_data.right
            self.root.parent = None
        self.rbt_tree_set_child(node_data.left, "right", node_data)
        self.rbt_tree_set_child(node_data, "left", left_r_child)

    @staticmethod
    def rb_grandparent(node):
        if node.parent is None:
            return None
        return node.parent.parent

    @staticmethod
    def rb_uncle(node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def rbt_balance_tree(self, node_data):
        if node_data.parent is None:
            node_data.color = "black"
            return
        if node_data.parent.color == "black":
            return
        parent = node_data.parent
        grandparent = self.rb_grandparent(node_data)
        uncle = self.rb_uncle(node_data)
        if uncle is not None and uncle.colot == "red":
            parent.color = uncle.color = "black"
            self.rbt_balance_tree(grandparent)
            return
        if node_data is parent.right and parent is grandparent.left:
            self.rbt_tree_rotate_right(parent)
            node_data = parent
            parent = node_data.parent
        elif node_data is parent.left and parent is grandparent.right:
            self.rbt_tree_rotate_right(parent)
            node_data = parent
            parent = node_data
        parent.color = "black"
        grandparent.color = "red"
        if node_data is parent.left:
            self.rbt_tree_rotate_right(grandparent)
        else:
            self.rbt_tree_rotate_left(grandparent)

    '''
    insert the item in the corresponding place
    '''

    def insert_item(self, data):
        new_item = Node(data)
        if self.root is None:
            self.root = new_item
            self.root.color = "black"  # default color
            new_item.height = new_item.height + 1
            return

        new_item.height = new_item.height + 1
        current_node = self.root
        while current_node is not None:
            if new_item.item < current_node.item:
                if current_node.left is None:
                    current_node.left = new_item
                    new_item.parent = current_node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_item
                    new_item.parent = current_node
                    current_node = None
                else:
                    current_node = current_node.right
        new_item.color = "red"
        while new_item is not None:
            self.rbt_tree_update_height(new_item)
            new_item = new_item.parent


def bst_search(word):
    c = avl()
    if c.root is None or c.root == word:
        return True
    if c.root.item < word:
        return c.bst_search(c.root.left, word)
    elif c.root.item > word:
        return c.bst_search(c.root.right, word)
    return False


def print_anagrams(word, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        if bst_search(str):
            print(prefix + word)
            return prefix + word
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur)


def avl_method(user_input, file, word):
    call = avl()
    line = file.readline()
    while line:
        line = file.readline()

        call.insert_item(line)

    file.close()
    print_anagrams(word)


'''
avl_method read the text file line by line and insert it to the corresponding 
tree
RBTree reads the the text file and insert it each value in the tree 
'''


def rbt_tree_method(user_input, file, word):
    call = RBTree()
    line = file.readline()
    while line:
        line = file.readline()
        call.insert_item(line)
    file.close()
    print_anagrams(word)


'''
ask the user which tree they want to uses call the corresponding methods
'''


def main():
    file = open("TestWord.txt")
    print("please choose an option:")
    print("A.avl")
    print("B.RBlackTree")
    user_input = input()
    word = input("input a word you want to fine :")
    if user_input == "A" or user_input == "a":
        avl_method(user_input, file, word)

    elif user_input == "B" or user_input == "b":
        rbt_tree_method(user_input, file, word)


main()
