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
            # cursor.execute("UPDATE Ordenes SET ESTADO = '%s' WHERE ID = '%s'" % ("PAGADA",key))
        else:
            self.keys.append(key)
            bucket.append((key, val))
    # Return searched value with specific key
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
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):
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
            # the key to be deleted
            if str(record_key) == str(key):
                found_key = True
                break
        if found_key is True:
            # cursor.execute("DELETE FROM Ordenes WHERE ID = '%s'" % (key))
            bucket.pop(index)
        return (found_key)
            
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

# test = HashTable(10)
# test.set_val('t1', 'val1')
# test.set_val('t2', 'val2')

# # print(test.get_val('t1'))

# res = [{a: {b}} for (a, b) in zip(test.keys, test.get_val())]

# # printing result
# print("The constructed dictionary : " + str(res))