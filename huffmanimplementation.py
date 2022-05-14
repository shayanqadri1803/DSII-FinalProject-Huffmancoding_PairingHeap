from Tree import *
from pairingheap import * 

class Huffman(Tree):

    def __init__(self):

        self.huffmantree = None    #the main huffman encoding tree
        self.charlist = None
        self.txt_file_data = None
        self.encodedinfo = ''

    def get_huffmantree(self): 
        return self.huffmantree

    def set_huffmantree(self, hufftree): 
        self.huffmantree = hufftree

    def get_charlist(self): 
        return self.charlist

    def set_charlist(self, chars): 
        self.charlist = chars

    def get_txt_file_data(self):
        return self.txt_file_data

    def set_txt_file_data(self, data): 
        self.txt_file_data = data

    def get_encodedinfo(self): 
        return self.encodedinfo

    def set_encodedinfo(self, info): 
        self.encodedinfo = info