class Hashing:
    def __init__(self, keys):
        self.keys = keys
        self.hash_map = {}
    
    def hash_keys(self, show_computation = True):
        # initialize empty hash map
        for i in range(11):
            self.hash_map[i] = None
        if show_computation:
            print(f"Initial Array: {self.keys}\n")
            print(f"A empty hash map with 11 has been initialized\n")
            print(f"->{self.hash_map}\n\n")

        # map given keys
        for key in self.keys:

            remainder = key % 11
            if self.hash_map[remainder] == None:
                self.hash_map[remainder] = key
                if show_computation:
                    print(f"The position of key: {key} from initial Array is calculated with: k({key}) mod 11 = {remainder}\n")
                    print(f'-> The key: {key} has been inserted to slot: {remainder}\n')
                    print(f"-> new hash: {self.hash_map}\n\n")
                
            elif self.hash_map[remainder] != None:
                # first case using the quadratic probe
                probe_count = 0
                print(f"The position of key: {key} is calculated with: h(k,i) = (h(k) + 3(i)^2 +2 )mod 11\n")
                while True:
                    new_key = self.compute_quadratic_probe(key, remainder, probe_count)
                    if self.hash_map[new_key] == None:
                        break
                    probe_count += 1
                computed_probe = self.compute_quadratic_probe(key, remainder, probe_count, False)
                self.hash_map[computed_probe] = key
                print(f'-> The key: {key} has been inserted to slot: {computed_probe}\n')
                print(f"-> new hash: {self.hash_map}\n\n")
    
    def compute_quadratic_probe(self,key, remainder,probe_count, show_computation = True):
        if show_computation:
            print(f"""
    A colision has been encountered:

    The key: {key}

    k({key}) mod 11: {remainder}

    Iteration(i): {probe_count}

    Computing quadratic probe using
        h(k,i) = (h(k) + 3(i)^2 +2 )mod 11
        h(k,i) = ({key} + 3({probe_count})^2 +2 )mod 11
        h(k,i) = ({key} + {3*(probe_count**2)} +2 )mod 11
        h(k,i) = ({remainder + 3*(probe_count**2) + 2})mod 11
        h(k,i) = {(remainder + 3*(probe_count**2) + 2) % 11}
        
        """)
        return (remainder + 3*(probe_count**2) + 2) % 11
    
    def get_hash_map(self):
        if len(self.hash_map) == 0:
            print('Hash map is empty, run has_keys function')
            return
        print(f"final hashmap: {self.hash_map}")
        return self.hash_map
