class HashMap():
    def __init__(self):
        self.hahsmap_size = 32
        self.hashmap_data = [None] * self.hahsmap_size

    def __get_hash_mod_size(self, key):
        hash_key_var = hash(key+str(self.hahsmap_size*0.01))
        return hash_key_var % self.hahsmap_size

    def set_key_value(self, key, value):
        key_var = self.__get_hash_mod_size(key)
        key_value_list = [key, value]

        if self.hashmap_data[key_var] is None:
            self.hashmap_data[key_var] = list([key_value_list])
            return True
        else:
            for pair in self.hashmap_data[key_var]:
                print(pair)
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashmap_data[key_var].append(key_value_list)
            return True

    def get_key(self, key):
        key_var = self.__get_hash_mod_size(key)
        if self.hashmap_data[key_var] is not None:
            for pair in self.hashmap_data[key_var]:
                if pair[0] == key:
                    return pair[1]
            return None

    def remove_key(self, key):
        key_var = self.__get_hash_mod_size(key)

        if self.hashmap_data[key_var] is not None:
            return False
        for i in range(len(self.hashmap_data[key_var])):
            if self.hashmap_data[key_var][i][0] == key:
                self.hashmap_data[key_var].pop(i)
                return True
    def print_hashmap(self):
        for item in self.hashmap_data:
            if item is not None:
                print(item)


hm = HashMap()
hm.set_key_value('A', '1')
hm.set_key_value('A', '2')
hm.set_key_value('B', '1')
hm.set_key_value('A', '3')
hm.set_key_value('A', '4')
hm.set_key_value('C', '1')
hm.set_key_value('D', '1')
hm.set_key_value('E', '1')
hm.set_key_value('E', '2')
hm.remove_key('A')
hm.remove_key('B')
hm.remove_key('B')
print('rere')
hm.print_hashmap()