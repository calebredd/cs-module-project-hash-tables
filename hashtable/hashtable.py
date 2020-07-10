class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def findKey(self):
        current = self.head
        if current is not None:
            return current.key
        return None

    def insert(self, key, value):
        node = HashTableEntry(key, value)
        if self.head is None:
            self.head = node
            return self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            return  current.next
    
    def overwrite(self, key, value):
        current = self.head
        if current.key == key:
            current.value = value
            return
        while current.next is not None:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        if current.key == key:
            if current.next is not None:
                self.head = current.next  
            else:
                self.head = None
        else:
            while current.next is not None:
                if current.next.key == key:
                    if current.next.next is not None:
                        current.next = current.next.next
                        return
                    else:
                        current.next = None
                        return
                current = current.next
        return None
        

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else: self.capacity = 8
        self.hash_table = [None] * self.capacity
        self.counter = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.counter/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # string_bytes = key.encode()
        # total = 0
        # for b in string_bytes :
            # total += b
        # return total
        hash = 5381
        for b in key:
            hash = (hash * 33 ) + ord(b)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Add a counter for tracking resizing, but don't add to the count if overwriting a key
        # Check load factor, if great than 0.7, refactor and double the capacity.
        
        h = HashTableEntry(key, value)
        # ll = LinkedList() initiated down below after classes
        hashedKey = self.hash_index(key)
        if self.hash_table[hashedKey] is not None:
            #  ll already exists at that index, add to it
            if self.hash_table[hashedKey].find(key) is not None:
                self.hash_table[hashedKey].overwrite(key, value)
            else:
                self.hash_table[hashedKey].insert(key, value)
                self.counter += 1
        else:
            # ll doesn't exist, create one at this index, insert your item as the head
            self.hash_table[hashedKey] = LinkedList()
            self.hash_table[hashedKey].insert(key, value)
            self.counter += 1
        if self.get_load_factor() > 0.7:
            # print(self.get_load_factor())
            self.resize(self.capacity*2)
            
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Stretch goal: 
        # Use the counter for tracking resizing, decrement when deleting
        # Check load factor, if less than 0.2, rehash to half the size with atleast the minimum capacity

        hashedKey = self.hash_index(key)
        if self.hash_table[hashedKey].find(key): 
            self.counter -=1
            self.hash_table[hashedKey].delete(key)  
        # if self.get_load_factor() < 0.2:
            # self.resize(self.capacity/2)
        return


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hashedKey = self.hash_index(key)
        return self.hash_table[hashedKey].find(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        newTable=[None] * new_capacity
        for h in self.hash_table:
            while h is not None and h.findKey() is not None:
                key = h.findKey()
                value = h.find(h.findKey())
                rehashedKey = self.hash_index(key)
                h.delete(key)
                if newTable[rehashedKey] is not None:
                    newTable[rehashedKey].insert(key, value)
                else:
                    newTable[rehashedKey] = LinkedList()
                    newTable[rehashedKey].insert(key, value)
        self.hash_table = newTable
        return
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
