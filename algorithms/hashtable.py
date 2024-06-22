from dataclasses import dataclass, field

@dataclass()
class HashTables:
    key: str
    value: str
    __table: list = field(init=False, default_factory = lambda: [None] * 16)
    __keys: list = field(init=False, default_factory = list)
    
    #def __post_init__(self):
        #object.__setattr__(self, '_HashTables__table', [None] * self.__size)
    
    def get_index(self, a_string: str) -> int:
        result = 0
        for a_character in a_string:
            a_number = ord(a_character)
            result += a_number
        list_index = result % len(self.__table)
        return list_index
    
    '''
    1. If the position is none then the result is position from get_index.
    2. If the position is already occupied then the hash is changed.
    3. If the position == start position i.e., if it is 
    '''
    def get_valid_index(self, key: str) -> int:
        position = self.get_index(key)
        start_position = position
        while self.__table[position] is not None:
            stored_key, _ = self.__table[position]
            if stored_key == key:
                break
            position = (position + 1) % len(self.__table)
            if position == start_position:  # We have looped around the table
                raise Exception("Hash table is full")
        return position
    
    '''Insert into the hash table : Implement the hash table insert function:
    1. Check the key calculate the get_index and then use it to put the value into the poisition
    2. Handle collisions'''

    def insert(self, key, value):
        self.__keys.append(key)
        position = self.get_valid_index(key)
        self.__table[position] = (key,value)
        return self.__table
    
    
    def find(self, key):
        position = self.get_valid_index(key)
        return self.__table[position][1]
    
    
    def update(self, key, value):
        position = self.get_valid_index(key)
        self.__table[position] = (key,value)

    @property
    def list_all(self):
        return self.__keys

    

hash_table = HashTables( key = "exampleKey", value = "exampleValue" )
hash_table.insert('raman','9493946069')
hash_table.insert('manar','8')
print (hash_table.find('raman'))
print (hash_table.list_all)


