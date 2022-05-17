from hufftree import Tree
from Pairingheapstructure import * 


class Huffman(Tree):

    def __init__(self):

        self.huffmantree = None    #the main huffman encoding tree
        self.charlist = None       #includes the character and their frequencies
        self.txt_file_data = None
        self.encodedinfo = ''

    def set_huffmantree(self, hufftree): 
        self.huffmantree = hufftree

    def set_charlist(self, chars): 
        self.charlist = chars

    def set_txt_file_data(self, data): 
        self.txt_file_data = data

    def set_encodedinfo(self, info): 
        self.encodedinfo = info


    def create_huffman_tree(self, inpt):
        """ this function iterates over all the tuples of type (character, frequency)
        and creates a tree by adding the least two frequencies using top function of pairing heap
        returns a value of type [(rootnode), a list of (character,frequency)]"""

        characters = '\'"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890!@#$%^&*()-_+={[}]\|<>,.?/~`\n'
        # arrays that keep track of the counted characters and the trees
        chars_count=PairingHeap()
        temp_chars_count=[]
        baseTrees = []
        # if the character in the list is in the input it counts it and appends it to list
        for char in characters:
            x = inpt.count(char)
            if char in inpt:
                temp_chars_count.append([char, inpt.count(char)])
                chars_count.insert([char, inpt.count(char)])

        # makes a base tree for each counted letter
        for iter in temp_chars_count:
            baseTrees.append(Tree(None, None, chars_count.find_min()))
            chars_count.delete_min()
        tree1 = baseTrees

        # joins the trees together into a binary tree
        while len(tree1) > 1:
            #if both current nodes are of type list ["E", 6] 
            if type(tree1[0].get_mid()) == list and type(tree1[1].get_mid()) == list: 
                a = tree1[0].get_mid()[1] 
                b = tree1[1].get_mid()[1]

            elif type(tree1[0].get_mid()) == int and type(tree1[1].get_mid()) == int: 
                a = tree1[0].get_mid()
                b = tree1[1].get_mid()

            elif type(tree1[0].get_mid()) == int and type(tree1[1].get_mid()) == list: 
                a = tree1[0].get_mid()
                b = tree1[1].get_mid()[1]
                
            elif type(tree1[0].get_mid()) == list and type(tree1[1].get_mid()) == int:     
                a = tree1[0].get_mid()[1]
                b = tree1[1].get_mid()
               
            newCurrent = a + b  #new root node from above example 
            newLeft = tree1[0]  #assign left child of current node
            newRight = tree1[1] #assign right child of current node
            newTree = Tree(newLeft, newRight, newCurrent) #newtree made using newleft, newright and newcurrent 
            tree1.append(newTree)
            tree1.remove(newTree.get_left()) #used nodes that we are deleting 
            tree1.remove(newTree.get_right())
            tree1.sort(key=self.getkey)

        self.set_huffmantree(tree1[0])
        self.set_charlist(temp_chars_count)
        self.set_txt_file_data([tree1[0], chars_count])
        return [tree1[0], temp_chars_count]

    

