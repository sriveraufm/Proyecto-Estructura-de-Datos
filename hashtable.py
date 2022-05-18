class HashTable:
    
	# Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        self.keys = []

    def create_buckets(self):
        return [[] for _ in range(self.size)]

	# Insert values into hash map
    def set_val(self, key, val):
		
		# Get the index from the key
		# using hash function
        hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        
        for index in range(len(bucket)):
            record = bucket[index]
            record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            self.keys.append(key)
            bucket.append((key, val))
    def delete(self, key):
        hashed_key = hash(key) % self.size
        self.hash_table[hashed_key] = []
        self.keys.remove(key)
    def get_val(self, key):
    # Get the index from the key using
    # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index in range(len(bucket)):
            record = bucket[index]
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return None
    def exists(self, key):
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        if len(self.hash_table[hashed_key]) > 0:
            return True
        else:
            return False
    def get_table(self):
        return list(filter(None, self.hash_table))
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
        # return self.hash_table

# test = HashTable(3)
# test.set_val('t1', {'val1':131, 'val2': 'tetet', 'val3': 'saber'})


# print(test.get_table())
# print(test.keys)

# # print(test.get_table())
# print(test.get_val('t1')['val1'])

#Fuente: https://www.geeksforgeeks.org/hash-map-in-python/
