#implementing hash map in python

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None]*self.size#just a list that can be extended

    def _get_hash(self,key):
        hash = 0
        for c in str(key):
            hash+=ord(c)
        return hash % self.size

    def add(self,key,value):
        key_hash = self._get_hash(key)
        print('adding by hash %d' % key_hash)
        key_value = [key,value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
        
    def get(self,key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
        

    def keys(self):
        print('------KEY ----')
        a = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                a.append(self.map[i][0])
        return a

    def print(self):
        print('----- HASH MAP CONTENT------')
        for item in self.map:
            if item is not None:
                print(str(item), sep = ' ')
            else:
                print('Null hash')
                


#if "__name__" == "__main__" :
    
r = HashMap()

r.add('Erjan', '324234')
r.add('Ming', '29303')
r.add('Bob', '11111')
r.add('Tair', '22222')
r.add('Aliciya', '33333')
r.add('azat', '42343')

r.print()
print(r.keys())
