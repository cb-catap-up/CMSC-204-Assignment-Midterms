from binary_search_tree.BinarySearchTree import BST 
from avl_tree.AVLTree import AVL
import time
from heaps.Heap import Heap
from hashing.Hashing import Hashing
from helpers.Helpers import clear_console


class Application():
    def __init__(self):
        super().__init__

    def start_screen(self):
        START_SCREEN = """
            ╔════════════════════════════════════════════════════════════╗
            ║                                                            ║
            ║          MEDICAL CARAVAN QUEUE SYSTEM                      ║
            ║                                                            ║
            ║                    🏥 Bayan ng Anda                        ║
            ║                    📋 Lalawigan ng Pangasinan              ║
            ║                    👥 2026                                 ║
            ║                                                            ║
            ╚════════════════════════════════════════════════════════════╝
            """
        print(f'{START_SCREEN}\n')
        time.sleep(5)
        clear_console()
        
        print('🦠' * 50)
        print('💻' * 50)
        print(f'Threat Simulation')
        print('👾' * 50)
        time.sleep(1)
        print('💻' * 50)
        time.sleep(1)
        print('🦠' * 50)
        time.sleep(1)
        print('👾' * 50)
        print(f'Found three threats!')
        time.sleep(1)
        print('💻' * 50)
        time.sleep(1)
        print(f'Additional three threats!')
        print('🦠' * 50)
        time.sleep(1)
        print('🦠' * 50)
        time.sleep(1)
        print('🦠' * 50)      
        print(f'FOUND A TOTAL OF 8 THREATS⚠️⚠️⚠️')
        time.sleep(2)           


    def menu_answer_1(self, keys, num_key=8):

        while True:
            print('Press 1 to see the threats inside a Binary Search Tree.')  
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        bst_start = BST()
        for key in keys:
            bst_start.insert(key)

        while True:
            print('Press 1 to balance the threat from BST to AVL Tree.')
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        avl_start = AVL()
        for key in keys:
            avl_start.insert(key)    

        while True:
            print('Press 1 to Convert the original threats into a max-heap')
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        heap = Heap(keys)
        heap.max_heap(show_process=True)

        while True:
            print('Press 1 to neutralize threats(2)')
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        heap.neutralize(num_to_neutralize=int(2))

        while True:
            print('Press 1 to store these threats to the hash table')
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        hasher = Hashing(keys)
        hasher.hash_keys()
        hasher.get_hash_map()

        while True:
            print('Press 1 to display the threats stored in AVL Tree in descending order:')
            answer = input(': ')            
            if answer == '1':
                clear_console()
                break
            else:
                print('Please make sure to enter valid option only')

        avl_start.display_descending_visualized()
        

if __name__ == "__main__":
    # Login.show_start_screen()
    start = Application()
    # start.clear_console()
    start.start_screen()
    # start = Application()
    # start.application() 
    # keys
    start.menu_answer_1([2,5,3,0,1,0,4,6])