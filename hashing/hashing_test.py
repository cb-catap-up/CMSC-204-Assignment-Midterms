from hashing.Hashing import Hashing

"""
    -This file is for testing 
    -this shows how functions are used

"""
def show_hashing_function(items):
    new_hash = Hashing(items)
    new_hash.hash_keys()
    _ = new_hash.get_hash_map()
