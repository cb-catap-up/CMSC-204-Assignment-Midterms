import heapq
from heaps.Heap import Heap


"""
    -This file is for testing 
    -using python built in heap library to check if heap is correct
    -this also shows how functions are used

"""


def is_min_heap_function_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.min_heap()

    # test cases
    test_keys = keys
    heapq.heapify(test_keys)

    print(f"is min heap correct: {new_heap.get_heap() == test_keys}")

def is_max_heap_function_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap(False)

    # test cases
    test_keys = keys
    heapq._heapify_max(keys)
    print(f"is max heap correct: {new_heap.get_heap() == test_keys}")


def is_peek_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap(False)

    # test cases
    test_keys = keys
    heapq._heapify_max(test_keys)


    print(f"is peek heap correct: {new_heap.peek() == heapq.nlargest(1,test_keys)[0]}")

def is_pop_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap(show_process=False)
    item = new_heap.pop(show_process=False)

    # test cases
    test_keys = keys
    max_heap = [-n for n in test_keys]
    heapq.heapify(max_heap)
    max_val = -heapq.heappop(max_heap)

    print(f"is pop correct: {(max_val ==item)}")

def is_neutralize_correct(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap(show_process=False)
    new_heap.neutralize(show_process=False)


    # test cases
    test_keys = keys
    max_heap = [-n for n in test_keys]
    heapq.heapify(max_heap)
    _ = -heapq.heappop(max_heap)
    _ = -heapq.heappop(max_heap)

    print(f"is neutralize correct: {[abs(x) for x in max_heap] == new_heap.heap}")

def show_min_heap(keys: list):
    new_heap = Heap(keys)
    new_heap.min_heap()

def show_max_heap(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap()

def show_max_peek(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap()
    new_heap.peek()

def show_min_peek(keys: list):
    new_heap = Heap(keys)
    new_heap.min_heap()
    new_heap.peek()

def show_pop(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap()
    _ = new_heap.pop()

def show_neutralize(keys: list):
    new_heap = Heap(keys)
    new_heap.max_heap()
    new_heap.neutralize()

