
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.hash(key)

        if not self.map[idx]:
            self.map[idx] = [[key, value],]
        else:
            self.map[idx].append([key, value])

    def get(self, key):
        idx = self.hash(key)


        if self.map[idx]:
            for el in self.map[idx]:
                if el[0] == key:
                    return el[1]
        else:
            return None
            

    def contains(self, key):
        idx = self.hash(key)

        if self.map[idx]:
            for el in self.map[idx]:
                if el[0] == key:
                    return True
        return False

    def hash(self, key):
        ascii_total = 0

        for ch in key:
            ascii_total += ord(ch)
        hashed = ascii_total * 17
        hashed = hashed % self.size

        return hashed



if __name__=='__main__':
    ht = Hashtable(1024)
    ht.add('name', 'batool')
    print (ht.hash('name'))
    print(ht.get('name'))