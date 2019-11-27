from Heap import MaxHeap
from LRC import LRC


def main(a):
    if a == 1:
        lrc = LRC(5)

        lrc.put("A", 0)
        lrc.put("B", 1)
        lrc.put("C", 2)
        lrc.put("D", 3)
        lrc.put("E", 4)
        lrc.put("F", 5)

        temp = lrc.head
        while temp is not None:
            print(temp.key + " -> ", end="")
            temp = temp.next
    else:
        hp = MaxHeap()
        hp.insert("apple")
        hp.insert("cherry")
        hp.insert("grapes")
        hp.insert("grapes")
        hp.insert("grapes")
        hp.insert("banana")
        hp.insert("banana")
        for i in range(len(hp.tree)):
            print(str(hp.tree[i].word) + " " + str(hp.tree[i].occur))

main(1)
