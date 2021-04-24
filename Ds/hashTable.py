class HashTable:
    def __init__(self, size):
        self.data = [None]*size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def add(self, key, value):
        addr = self._hash(key)
        if self.data[addr] is None:
            self.data[addr] = []
        self.data[addr].append([key, value])
        return self.data

    def get(self, key):
        addr = self._hash(key)
        currentBucket = self.data[addr]
        if len(currentBucket):
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None

    def keys(self):
        if len(self.data) is None:
            return None
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i] is not None:
                if len(self.data) > 1:
                    for j in range(len(self.data[i])):
                        keysArray.append(self.data[i][j][0])
                else:
                    keysArray.append(self.data[i][0])
        return keysArray


myHashTable = HashTable(50)
myHashTable.add('grapes', 10000)
# print(myHashTable.get('grapes'))
myHashTable.add('apples', 54)
# print(myHashTable.get('apples'))
myHashTable.add('oranges', 2)


print(myHashTable.keys())