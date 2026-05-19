from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

#here are my heap functions lovingly modified from lab 7 shoutout to prof. duran

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap.data[:]
    if index == 0:
        return MinHeap(new_heap)
    parent = (index - 1) // 2
    if new_heap[index] < new_heap[parent]:
        temp = new_heap[index]
        new_heap[index] = new_heap[parent]
        new_heap[parent] = temp
        return heapify_up(MinHeap(new_heap), parent)
    return MinHeap(new_heap)

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_heap = MinHeap(heap.data + [element])
    new_heap = heapify_up(new_heap, len(new_heap.data) - 1)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_heap = heap.data[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_heap)
    if left >= size:
        return MinHeap(new_heap)
    smallest = left
    if right < size and new_heap[right] < new_heap[left]:
        smallest = right
    if new_heap[smallest] < new_heap[index]:
        temp = new_heap[index]
        new_heap[index] = new_heap[smallest]
        new_heap[smallest] = temp
        return heapify_down(MinHeap(new_heap), smallest)
    return MinHeap(new_heap)


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    min_value = heap.data[0]
    last_value = heap.data[-1]
    new_heap = [last_value] + heap.data[1:-1]
    new_heap = heapify_down(MinHeap(new_heap), 0)
    return MinHeap(new_heap.data), min_value

def count_frequency(s: str)-> dict[str,int]:
    s_copy = list(s)
    frequency = {}
    for item in s_copy:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    new_minheap = MinHeap()
    for key, value in frequency.items():
        new_minheap = insert(new_minheap, Node(value, key))
    return new_minheap

def build_tree(priority_queue: MinHeap) -> Node|None:
    if len(priority_queue.data) == 0:
        return None
    if len(priority_queue.data) == 1:
        return priority_queue.data[0]
    first_extract, left = extract_min(priority_queue)
    second_extract, right = extract_min(first_extract)
    combined_node = Node(left.freq + right.freq,
                         min(left.char, right.char),
                         left,
                         right)
    rest = insert(second_extract, combined_node)
    return build_tree(rest)

def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}
    if node is None:
        return code
    if node.left is None and node.right is None:
        if prefix == "":
            code[node.char] = "0"
        code[node.char] = prefix
    generate_codes(node.left, prefix + "0", code)
    generate_codes(node.right, prefix + "1", code)
    return code

def encode(s: str, codes: dict)-> str:
    new_string = ""
    for char in s:
        new_string += codes[char]
    return new_string

def decode(encoded_string: str, root: Node):
    decoded = ""
    place_marker = root
    for char in encoded_string:
        if char == "0":
            place_marker = place_marker.left
        else:
            place_marker = place_marker.right
        if place_marker.left is None and place_marker.right is None:
            decoded += place_marker.char
            place_marker = root
    return decoded

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

