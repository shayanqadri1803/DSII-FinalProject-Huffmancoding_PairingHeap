# DSII-FinalProject-Huffmancoding_PairingHeap

Overview

This project implements a Huffman Coding system using a Pairing Heap data structure, providing an efficient method for data compression and decompression. Huffman Coding is a popular algorithm used to compress data by encoding characters based on their frequencies in the given data set. The project combines the Huffman Coding algorithm with a Pairing Heap, a type of priority queue, to create an optimized encoding and decoding process.

Key Components

	1.	Tree Structure:
	•	The Tree class represents the binary tree structure used in Huffman Coding, where each node can have a left and right child. The tree is constructed based on character frequencies, with lower-frequency characters deeper in the tree.
	2.	Pairing Heap:
	•	The Pairing Heap is used as a priority queue to efficiently manage the characters’ frequencies. The heap ensures that the characters with the lowest frequencies are always merged first, which is a key step in building the Huffman tree.
	3.	Huffman Class:
	•	This class is the core of the project, managing the entire process from encoding to decoding. It includes methods for creating the Huffman tree, encoding text into binary, compressing the encoded data, and then decompressing and decoding it back to its original form.
