from heaps.heap_test import (is_min_heap_function_correct, 
                             is_max_heap_function_correct,is_peek_correct, 
                             is_pop_correct, is_neutralize_correct, 
                             show_min_heap, 
                             show_max_heap, 
                             show_neutralize, 
                             show_max_peek,
                             show_min_peek,
                             show_pop)
from hashing.hashing_test import show_hashing_function

"""
    -This file is for testing 
    -Comment the ones not being tested to avoid clutter when testing

"""
test_inputs_array_hashing = [
    [3, 6, 1, 0, 2, 0, 5, 4],
    [0, 2, 3, 6, 5, 1, 4, 0],
    [1, 4, 0, 2, 3, 0, 6, 5],
    [5, 0, 2, 1, 4, 3, 6, 0],
    [2,5,3,0,1,0,4,6]

]

test_inputs_array_heaps = [
    [0, 3, 5, 2, 6, 1, 4, 0],
    [14, 1, 16, 2, 3, 10, 8, 7, 4, 9],
    [7, 16, 10, 4, 8, 3, 1, 14, 2, 9],
    [2, 0, 6, 4, 5, 1, 3, 0],
    [2,5,3,0,1,0,4,6]
]

def test_all_heap_functions(items):
    # is_min_heap_function_correct(items)
    # print('\n')
    is_max_heap_function_correct(items)
    print('\n')
    is_peek_correct(items)
    print('\n')
    is_pop_correct(items)
    print('\n')
    # is_neutralize_correct(items)
    # print('\n')

def show_all_processes(items):

    show_min_heap(items)
    show_max_heap(items)
    show_max_peek(items)
    show_min_peek(items)
    show_pop(items)
    show_neutralize(items)


def show_hashing(items):
    show_hashing_function(items)



def test_with_different_inputs():

    # testing Heaps
    for i in range(len(test_inputs_array_heaps)):
        print(f"\n--------------------------------------test {i + 1} Heaps Start------------------------------------------------------------\n\n")
        test_all_heap_functions(test_inputs_array_heaps[i])
        show_all_processes(test_inputs_array_heaps[i])
        print(f"\n--------------------------------------test {i + 1} Heaps End---------------------------------------------------------------\n\n")
    # testing hashing
    for i in range(len(test_inputs_array_hashing)):
        print(f"\n--------------------------------------test {i + 1} Hashing Start------------------------------------------------------------\n\n")
        show_hashing(test_inputs_array_hashing[i])
        print(f"\n--------------------------------------test {i + 1} Hashing End--------------------------------------------------------------\n\n")

# runs tests
test_with_different_inputs()
