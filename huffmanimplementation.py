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

    def getkey(self, x):
        """this function should return the int value of 
        the node and must accomodate list and int values"""
        #if type== int, returns int 
        if type(x.get_mid()) == int: 
            return x.get_mid()

        #if type == list, returns frequency 
        elif type(x.get_mid()) == list: 
            return x.get_mid()[1] 

    def traverse_tree(self, data, goesleft, goesright, value, letterlst): # recursive function 
        """this function should iterate over the huffman tree and assign
        0 to the left branches and 1 to the right branches of the tree recursively 
        till we encounter a leaf node"""

        if len(letterlst) == len(data[1]): return letterlst
        if goesleft: value = value + '0' #if traversal goes left, add 0 to the string 
        if goesright: value = value + '1' #if traversal goes right add 1 to the string

        if type(data[0].get_mid()) == int:
            if type(data[0].get_left().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_left().get_mid()[0]:
                        if [i[0], str(value) + '0'] not in letterlst:
                            letterlst.append([i[0], str(value) + '0'])
                            
            if type(data[0].get_right().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_right().get_mid()[0]:
                        if [i[0], str(value) + '1'] not in letterlst:
                            letterlst.append([i[0], str(value) + '1'])
                             
            if type(data[0].get_left().get_mid()) == list and type(data[0].get_right().get_mid()) == list:
                for i in data[1]:
                    if i[0] == data[0].get_left().get_mid()[0]:
                        if [i[0], str(value) + '0'] not in letterlst:
                            letterlst.append([i[0], str(value) + '0'])
                            

                    if i[0] == data[0].get_right().get_mid()[0]:
                        if [i[0], str(value) + '1'] not in letterlst:
                            letterlst.append([i[0], str(value) + '1'])
                             
            return self.traverse_tree([data[0].get_left(), data[1]], True, False, value, letterlst) or \
                self.traverse_tree([data[0].get_right(), data[1]], False, True, value, letterlst)

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


    def encoding_txt_file(self, txt_file, encodedfile):
        """
        this function creates the huffman tree by calling the appropriate function
        and also assigns the binary code to each character of the tree, it should also
        concatenate all the codes into a single string and write it to a new binary file 
        in the form of a byte array. The output is the new binary encoded file

        """
        
        with open(txt_file, 'r+') as txtfile: #reading file
            with open(encodedfile, 'wb') as newtxtfile: #wb = write binary
                #removing all the whitespaces from the file since this wont affect the content and will reduce size
                strings = (txtfile.read()).rstrip()

                #building the huffman binary tree
                hufftree = self.create_huffman_tree(strings)
                #assigning codes to each character
                assign_codes = self.traverse_tree(hufftree, None, None, '', [])

                # assigning the codes list to the object it self
                self.set_charlist(assign_codes)
                #assigning the huffman tree to object itself
                self.set_huffmantree(hufftree)

                #concatenating the of each character in the text file to binary(bytes) form
                encoded_file = self.encoded_data(strings, assign_codes) 
                # if the encoded file is not divisible by 8, add extra 0's at the start of the file to create byte array
                fully_encoded_file = self.add_extra_bits(encoded_file)

                # getting byte array of the form b'\x04\xc7\xab_\x17tW\xa9\x13\x98
                byte_array = self.get_byte_array(fully_encoded_file)
                #writing the byte array to the new binary file i.e. our encoded file
                newtxtfile.write(byte_array)

    def decompressing_binary_file(self, file_to_decode):
        """This function takes input the binary file and reads
        bytes one by one from byte array, converts each byte 
        to bits and concatenates all of them.
        Must remove all extra start and end bits to get the original file.
        The output is a string of bits representing original file"""
        with open(file_to_decode, 'rb') as inputfile: #rb = read binary file
            #this variable will contain letters converted from bytes
            bit_text = ""
            #reading only 1 byte from the byte_array of our compressed or encoded file
            compressed_char = inputfile.read(1)

            #running a while loop till we reach the end of file
            while compressed_char != b'':

                #returning the number representing the unicode code of the byte 
                print(compressed_char)
                compressed_char = ord(compressed_char)
                #returning the binary equivalent of the given character
                bits = bin(compressed_char)
                #print(bits)
                #the binary number is of form "0b1110111" so removing the intial two characters i.e. "0b" to get bits only
                bits=bits[2:]

                #if the length of bits is not 8, add 0's at front
                if len(bits)<8:
                    for i in range(8-len(bits)):
                        bits='0'+bits
                
                #concatenating each character's bits to a single string
                bit_text += bits

                #reading the next byte of the byte array
                compressed_char = inputfile.read(1)

            #converting the last byte into integer to remove the extra data we added while encoding
            complete_data_and_info = bit_text[:8]
            additional_end_bits = int(complete_data_and_info, 2)

            #the full encoded data in bits excluding the first extra byte we added while encoding
            without_initial_bits = bit_text[8:]

            #getting the original file in bits without the extra data
            decompressed_text = without_initial_bits[:-1*additional_end_bits]

            #returning the original file in bits form
            return decompressed_text

    def decoding_decompressed_text(self, decompressed_txt, new_decoded_file):
        """this function writes the decoded data to a new text file 
        by iterating over all the bits and huffman tree till we encounter a
        letter."""
        #starting at the root of the tree
        current_element = self.huffmantree[0]

        #opening a new file to write back the data we encoded
        with open(new_decoded_file, 'w') as decodedfile:

            #taking the bit data and iterating bit by bit
            for bit in decompressed_txt:
                
                #checking if we have reached the leaf node or not i.e our character
                if type(current_element.get_mid())==int:

                    #if our bit was 0 means we have to go left
                    if int(bit) == 0:

                        #our new current node will then be the left child
                        current_element = current_element.get_left()
                    
                    #if our bit was 1 means we have to go right
                    if int(bit) == 1:
                        
                        #our new current node will then be the right child
                        current_element = current_element.get_right()

                #if we are on the leaf node then assign the character of the laf node to the decoded data and write to new file
                if type(current_element.get_mid())==list:

                    decodedfile.write(current_element.get_mid()[0])
                    #start again at the root of the node
                    current_element = self.huffmantree[0]

    def decode(self, encoded_file, output_file):
        """decompress and decode the binary file here by calling 
        appropriate functions"""
        #calling the decompression and decoding functions here
        decompressed = self.decompressing_binary_file(encoded_file)
        self.decoding_decompressed_text(decompressed, output_file)

# h = Huffman()
# h.encoding_txt_file('huff.txt', 'encoded.bin')
# h.decode('encoded.bin', 'decoded')
# h.inspect_tree(h.txt_file_data)
