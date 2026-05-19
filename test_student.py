import unittest
from proj3 import *

class TestSophia(unittest.TestCase):

    def test_heapify_up_normal(self):
        heap = MinHeap([Node(5, "e"), Node(3, "c"), Node(8, "h")])
        new_heap = heapify_up(heap, 1)
        self.assertEqual(new_heap.data[0], Node(3, "c"))
        self.assertEqual(len(new_heap.data), 3)
        self.assertEqual(heap.data[0], Node(5, "e"))

    def test_insert_normal(self):
        heap = MinHeap([Node(4, "d"), Node(6, "f")])
        new_heap = insert(heap, Node(2, "b"))
        self.assertEqual(new_heap.data[0], Node(2, "b"))
        self.assertEqual(len(new_heap.data), 3)
        self.assertEqual(len(heap.data), 2)

    def test_extract_min_normal(self):
        heap = MinHeap([Node(1, "a"), Node(3, "c"), Node(2, "b")])
        new_heap, smallest = extract_min(heap)
        self.assertEqual(smallest, Node(1, "a"))
        self.assertEqual(len(new_heap.data), 2)
        self.assertEqual(new_heap.data[0].freq, 2)

    def test_build_tree_normal(self):
        frequency = {"a": 2, "b": 1}
        pq = create_priority_queue(frequency)
        root = build_tree(pq)
        self.assertEqual(root.freq, 3)
        self.assertEqual(root.left.char, "b")
        self.assertEqual(root.right.char, "a")

    def test_encode_decode_simplelikeabc123(self):
        s = "aaabbc"
        encoded, decoded, codes = huffman_encoding(s)
        self.assertEqual(decoded, s)
        self.assertEqual(len(codes), 3)

    def test_single_character(self):
        s = "aaaa"
        encoded, decoded, codes = huffman_encoding(s)
        self.assertEqual(decoded, s)
        self.assertEqual(codes, {"a": "0"})
        self.assertEqual(encoded, "0000")

    def test_empty_string(self):
        s = ""
        encoded, decoded, codes = huffman_encoding(s)
        self.assertEqual(encoded, "")
        self.assertEqual(decoded, "")
        self.assertEqual(codes, {})


if __name__ == "__main__":
    unittest.main()