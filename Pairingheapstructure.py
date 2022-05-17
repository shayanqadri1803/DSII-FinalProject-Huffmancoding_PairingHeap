class HeapNode():
    # Creates the new node
    def __init__(self, value):
        self.value = value
        self.children = []

class PairingHeap():
    def __init__(self):
        self.root = None

    # Returns the value at the root of the Heap
    def find_min(self):
        if self.root:
            return self.root.value
        else:
            print ("Heap is empty!")

    # This Function is used to merge two heaps
    def merge(self, HeapA, HeapB):
        # If any of the two-nodes is None, returns the node that is NOT None
        if HeapA is None:
            return HeapB
        if HeapB is None:
            return HeapA
        # To maintain the min-heap condition comparethe nodes.
        # The node with minimum value becomes the parent of the other node   
        if type(HeapA.value)==int and type(HeapB.value)==int:
            if HeapA.value < HeapB.value:
                HeapA.children.append(HeapB)
                return HeapA
            HeapB.children.append(HeapA)
            return HeapB
        elif type(HeapA.value)==int and type(HeapB.value)==list:
            if HeapA.value < HeapB.value[1]:
                HeapA.children.append(HeapB)
                return HeapA
            HeapB.children.append(HeapA)
            return HeapB
        elif type(HeapA.value)==list and type(HeapB.value)==int:
            if HeapA.value[1] < HeapB.value:
                HeapA.children.append(HeapB)
                return HeapA
            HeapB.children.append(HeapA)
            return HeapB
        else:
            if HeapA.value[1] < HeapB.value[1]:
                HeapA.children.append(HeapB)
                return HeapA
            HeapB.children.append(HeapA)
            return HeapB
            
    # This Function inserts new values into the Node
    def insert(self, value):
        self.root = self.merge(self.root, HeapNode(value))

    # This Function deletes the root node of Heap
    def delete_min(self):
        if self.root is None:
            print("empty heap")
        else:
            self.root = self.merge_pairs(self.root.children)

    #This method is used when the root node is to be deleted, it merges two seperate heaps into one
    def merge_pairs(self, l):
        if len(l) == 0:
            return None
        elif len(l) == 1:
            return l[0]
        else:
            return self.merge(self.merge(l[0], l[1]), self.merge_pairs(l[2:]))

heap= PairingHeap()
heap.insert(3)
heap.insert(4)
heap.insert(1)
heap.insert(10)
heap.delete_min()
print(heap.find_min())
