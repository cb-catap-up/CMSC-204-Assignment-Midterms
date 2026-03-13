import math
from helpers.Helpers import add_break_point

class Heap:
    def __init__(self, keys):
        self.keys = keys
        self.heap = []
    def display_heap(self):
        """
        Display heap (works for heaps up to 4 levels)
        """

        if not self.heap:
            print("Heap is empty")
            return
        nodes = self.get_current_nodes_for_each_level()
        number_of_node_statements = len(nodes)
        node_number_iterator = 1
        next_node_index_to_print = 0

        separator_for_1_first_level = "/   \\"
        separator_for_1_second_level = "/     \\"
        separator_for_1_third_level = "/       \\"
        separator_for_1_fourth_level = "/         \\"

        second_single_spacer_unit = "/   "
        second_spacer_unit = "/   \\"

        count_third_layer = len(nodes[2])
        if count_third_layer == 2:
            second_spacer_unit_two = ""
        elif count_third_layer == 3:
            second_spacer_unit_two = f"{second_single_spacer_unit}"
        else:
            second_spacer_unit_two = second_spacer_unit

        # build separator dynamically
        separator_for_second_level = f"{second_spacer_unit}{' ' * 7}{second_spacer_unit_two}"

        separator_for_third_level = '/ \\'
        if number_of_node_statements == 4:
            third_spacer_single_unit = "/ "
            third_spacer_unit = "/ \\"

            count = len(nodes[3])

            groups = count // 2

            spacers = [third_spacer_unit] * groups

            # if odd number of nodes, add single branch pieces
            if count % 2 == 1:
                spacers.append(third_spacer_single_unit)

            separator_for_third_level = (" " * 3).join(spacers)

        second_level_spacer = 11 * " "
        third_level_spacer = 5 * " "
        fourth_level_spacer = 3 * " "
        inbetween_spacer = " "

        print(f"Current Heap: \n" )

        for i in range(number_of_node_statements):

            item_to_print = ""

            spacer = third_level_spacer
            
            item_counter = 1

            for _ in range(node_number_iterator):
                if next_node_index_to_print >= len(self.heap):
                    break

                if item_counter % 2 == 0:
                    spacer = inbetween_spacer
                    if i == 2:
                        spacer = inbetween_spacer *5
                else:
                    if i == 1:
                        spacer = second_level_spacer
                    elif i == 2:
                        spacer = third_level_spacer
                    elif i == 3:
                        spacer = fourth_level_spacer

                item_to_print += str(self.heap[next_node_index_to_print]) + spacer
                next_node_index_to_print += 1
                item_counter += 1

            if i == 0:
                print(f"{12*' '}{item_to_print}")
                print(f"{10*' '}{separator_for_1_first_level}")
                print(f"{9*' '}{separator_for_1_second_level}")
                print(f"{8*' '}{separator_for_1_third_level}")
                print(f"{7*' '}{separator_for_1_fourth_level}")
            elif i == 1:
                print(f"{6*' '}{item_to_print}")
                print(f"{4*' '}{separator_for_second_level}")
            elif i == 2:
                print(f"{3*' '}{item_to_print}")
                if number_of_node_statements == 4:
                    print(f"{2*' '}{separator_for_third_level}")
            else:
                print(f"{1*' '}{item_to_print}")

            node_number_iterator *= 2
        print("\n")

    def _get_last_parent_index(self, keys):
        # index of the last parent node
        return len(keys)//2-1

    def _get_parent_index(self, index):
        return (index)//2

    def _get_left_children_index(self, index):
        return 2*index + 1

    def _get_right_children_index(self, index):
        return 2*index + 2

    def _heapify_min(self,keys: list, index, show_process):
        while True:
            parent = index
            left_item = self._get_left_children_index(index)
            right_item = self._get_right_children_index(index)

            if left_item < len(keys) and keys[left_item] < keys[parent]:
                parent = left_item
            if right_item < len(keys) and keys[right_item] < keys[parent]:
                parent = right_item
            if parent == index:
                break

            if show_process:
                # show what is bubbling
                print(f"Movement: {keys[index]} bubble down, {keys[parent]} bubble up\n")

            keys[index], keys[parent] = keys[parent], keys[index]

            if show_process:
                # show heap after each swap
                self.display_heap()
                print('\n')

            index = parent
        return keys

    def min_heap(self, show_process=True):
        self.heap = self.keys.copy()
        if show_process:
            print("MININIMUM HEAP\n")
            # show array input
            print('original array:\n')
            print(f"{self.heap}\n")
            # show heap originally
            print('tree version of heap:\n')
            self.display_heap()
            print('\n')
    
        for i in range(self._get_last_parent_index(self.heap), -1, -1):
            self._heapify_min(self.heap, i, show_process)

    
    def max_heap(self, show_process = True):
        self.heap = self.keys.copy()
        if show_process:
            print("MAXIMUM HEAP\n")
            # show array input
            print('original array:\n')
            print(f"{self.heap}\n")
            # show heap originally
            print('tree version of heap:\n')
            self.display_heap()
            add_break_point(5, sleep_only=True)
    
        for i in range(self._get_last_parent_index(self.heap), -1, -1):
            self.heap = self.bubble_down(self.heap,i, show_process)
        if show_process:
            print(f"{'='*100}")

    def peek(self):
        print(f"PEEK OCCURED: {self.heap[0]}")
        return self.heap[0]

    # same as max heapify
    def bubble_down(self,keys, index, show_process, current_header=None):
        if show_process and current_header != None:
            print(current_header)

        while True:

            parent = index
            left_item = self._get_left_children_index(index)
            right_item = self._get_right_children_index(index)

            if left_item < len(keys) and keys[left_item] > keys[parent]:
                parent = left_item
            if right_item < len(keys) and keys[right_item] > keys[parent]:
                parent = right_item
            if parent == index:
                break
            if show_process:
                # show what is bubbling
                print(f"Movement: {keys[index]} bubble down, {keys[parent]} bubble up\n")

            keys[index], keys[parent] = keys[parent], keys[index]

            if show_process:
                # show heap after each swap
                self.display_heap()
                print('\n')
                add_break_point(5, sleep_only=True)
            index = parent
        return keys
    
    def get_current_nodes_for_each_level(self):
        if not self.heap:
            raise IndexError("no items from heap")

        height = math.floor(math.log2(len(self.heap)))

        levels = []
        index = 0
        total_nodes = len(self.heap)

        for level in range(height + 1):
            # start = 2**level - 1
            # end = min(2**(level + 1) - 2, len(self.heap) - 1)
            nodes_at_this_level = min(2**level, total_nodes - index)

            if nodes_at_this_level <= 0:
                break

            # current_level = self.heap[start:end+1]
            # levels.append(current_level)
            current_level = self.heap[index:index + nodes_at_this_level]
            levels.append(current_level)
            index += nodes_at_this_level
            
            if index >= total_nodes:
                break

        return levels


    def pop(self, show_process= True, current_header=None):
        if not self.heap:
            raise IndexError("pop from empty heap")
        
        if show_process:
            print("POP OCCURS\n")
            # show array input
            print('original array:\n')
            print(f"{self.heap}\n")
            # show initial
            self.display_heap()
            add_break_point(sleep_only=True)
        if show_process:
            print("Movement: Swap first and last index and remove the last index\n")
            print(f"{self.heap}\n")
            print("           |     ")
            print("           |     ")
            print("          \|/     \n")
        # Swap root with last element, then remove last element so it can bubble down
        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        item = self.heap.pop()  # Remove the max (old root)

        if show_process:
            # show heap after each swap
            print(f"{self.heap}\n")
            self.display_heap()
            print('\n')
            add_break_point(5, sleep_only=True)
        # # Bubble down the new root to restore heap property
        if self.heap:
            self.bubble_down(self.heap,0, show_process, current_header)
        # reassign new heap after using pop
        return item

    # remove the two larges values
    def neutralize(self, show_process=True, num_to_neutralize=2):
        if show_process:
            print("NEUTRALIZE OCCURS\n")
            # show array input
            print('original array:\n')
            print(f"{self.heap}\n")
            # show initial
            self.display_heap()
            add_break_point(sleep_only=True)
        for _ in range(num_to_neutralize):
            self.pop(show_process)
            add_break_point(5, sleep_only=True)
        print("NEUTRALIZED HEAP\n")
        self.display_heap()
        add_break_point(5, sleep_only=True)
    
    # returns heap
    def get_heap(self):
        return self.heap