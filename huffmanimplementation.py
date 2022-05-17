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
    
    def inspect_tree(self, data): 
        """this function should print the tree to help decode"""
        if data[0].get_left():
            if data[0].get_right(): #checking if left and right node are not None

                print(" Left: " + str(data[0].get_left().get_mid()) + "Mid Node: " + str(data[0].get_mid()) +
                        " Right: " + str(data[0].get_right().get_mid()))

                self.inspect_tree([data[0].get_right()])
                self.inspect_tree([data[0].get_left()])
                
      
    
    def encoded_data(self, text, listofcharacters): 
        """this function will convert all the letters
        to their respective codes and concatenate them
        the output will be the concatenated result in string form"""  
        #this will hold the result
        str_encode = '' 
        #iterating ove file characters
        for char in text: 
            #if the letter is in our assigned codes list then concatenate to result   
            for i in listofcharacters:  
                if char == i[0]:    
                    str_encode += i[1]  
        return str_encode

    def add_extra_bits(self, compressedtext):
        """format the encoded text in such a way that 
        we can divide it into bytes for byte array"""
        #finding out the length of extra bits
        extra_bits = (8 - len(compressedtext)) % 8

        #adding 0's to make it divisible by 8
        for i in range(extra_bits):
            compressedtext += "0"

        #adding an extra bit at the start to make it divisble by 8
        info = "{0:08b}".format(extra_bits)
        compressedtext = info + compressedtext
        self.set_encodedinfo(info)
        return compressedtext

    def get_byte_array(self, encode):
        """encode the bytes in the form 
        bytearray(b'\x00\x00\x00')"""
        #recheck if the bits are divisible by 8, otherwiese error is here
        if len(encode) % 8 != 0:
            print("bits not divisible")
        #initializing the byte array
        byte_array = bytearray()

        #iterate over ecode string with an iterator of 8
        for i in range(0,len(encode), 8):
            #store the 8 bits
            byte = encode[i:i + 8]
            #append them to bytearray
            byte_array.append(int(byte, 2))
        return byte_array
    

