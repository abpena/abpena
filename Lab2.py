class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.count = count
        self.password = password
        self.next = next


class SLL(object):
    head = None

    def __init__(self, head=None):
        self.head = None

    def append(self, x):
        # Inserts x at end of list L
        if is_empty(self):
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    # checks if is empty
    def is_empty(self):
        return self.head is None


# method checks for duplicate passwords and checks to see if it is empty
def BoolReplace(string, link):
    temp = link.head

    while temp is not None:
        if temp.password == string:
            temp.count += 1
            return True
        else:
            temp = temp.next

    return False


# reads file as well as creates all elements into a linked list
def Create():
    linkedlist = SLL()

    FileR = open("10-million-combos.txt", "r")
    line = FileR.readline()
    for line in FileR:

        line = line.strip().split("	")
        password = line[-1]

        # If password was not found:
        if not BoolReplace(password, linkedlist):
            linkedlist.head = Node(password, 1, linkedlist.head)

    FileR.close()

    tmp = linkedlist.head

    return linkedlist


# reads file as well as creates all elements into a dictionary
def CreateDic():
    passwordD = {}
    dictionary_llist = SLL()

    FileR = open("10-million-combos.txt", "r")
    line = FileR.readline()
    for line in FileR:

        line = line.strip().split("	")
        password = line[-1]

        if password in passwordD:
            passwordD[password].count += 1

        else:
            dictionary_llist.head = Node(password, 1, dictionary_llist.head)
            passwordD[password] = dictionary_llist.head

    FileR.close()
    tmp = dictionary_llist.head
    while tmp is not None:
        print(tmp.password, tmp.count)
        tmp = tmp.next


# method allows for only the top 20 passwords to be printed, will be used in merge and bubble sort
def print20(LList):
    temp = LList.head
    for i in range(20):
        print("Password: ", temp.password, "occurred ",
              temp.count, " amount of times")
        # i + 1
        temp = temp.next


# Splist instance of the list into two halves
def splitTheList(sourceList):
    if sourceList == None or sourceList.next == None:
        leftHalf = sourceList
        rightHalf = None

        return leftHalf, rightHalf

    else:
        midPointer = sourceList
        frontRunner = sourceList.next
        # totalLength += 1        - This is unnecessary

        while frontRunner != None:
            frontRunner = frontRunner.next

            if frontRunner != None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

    leftHalf = sourceList
    rightHalf = midPointer.next
    midPointer.next = None

    return leftHalf, rightHalf

# Merges both linked lists passed


def mergeTheLists(leftHalf, rightHalf):
    fake_head = Node(None)
    curr = fake_head

    while leftHalf and rightHalf:
        if leftHalf.val < rightHalf.val:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return fake_head.next

# Merge sort to head done by recursivly callig itself and split, then printing top 20


def mergeSortLinkedList(head):
    if head is None or head.next is None:
        return head

    leftHalf, rightHalf = splitTheList(head)

    left = mergeSortLinkedList(leftHalf)
    right = mergeSortLinkedList(rightHalf)

    print20(mergeTheLists(left, right))


# bubble sort would organize passwords in descending order with only top 20 printed
def bubble_sort(head):
    swap = True
    while swap:
        temp = head.head
        swap = False
        while temp.next is not None:
            if temp.count < temp.next.count:
                temp2 = temp.count
                temp.count = temp.next.count
                temp.next.count = temp2
                swap = True
            temp = temp.next

    print20(head)


# main
def main():
    x = SLL()
    x = Create()
    print("Linked list: \n")
    Create()
    print("Dictionary: \n")
    CreateDic()
    print("Bubble Sort: \n")
    bubble_sort(x)
    print("Merge Sort: \n")
    mergeSortLinkedList(x)


main()