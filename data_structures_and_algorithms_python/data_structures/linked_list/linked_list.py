
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else: 
            node.next = self.head
            self.head = node
        
    def includes(self, data):
        current = self.head
        while (current != None):
            if current.value == data:
                return True
            else:
                current = current.next
        return False
            
    def __str__(self):
        if self.head == None:
            return ("NULL")
        else:
            list = ""
            current = self.head
            while (current != None):
                list += '{ %s } -> ' %current.value
                current = current.next
            list += 'NULL'
            return (f"{list}")

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else: 
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            node = Node(newVal)
            if (self.head.value == value):
                return(self.insert(newVal))
            current = self.head
            while(current.next.value != value):
                current = current.next
            node.next = current.next
            current.next = node

    def insertAfter(self, value, newVal):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            node = Node(newVal)
            current = self.head
            while(current.value != value):
                current = current.next
            node.next = current.next
            current.next = node

    def deleteValue(self, value):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            current = self.head
            while(current.next.value != value):
                current = current.next
            current.next = current.next.next

        
        
    




####################################################
if __name__ == "__main__":
    myList = LinkedList()
    myList.append(0)
    myList.insert(5)
    myList.insert(3)
    myList.insert(1)
    myList.append(20)
    myList.append(22)
    myList.append(24)
    myList.insertBefore(1, 85)
    myList.insertAfter(24, 100)
    myList.insertAfter(85, 100)
    myList.insertAfter(0, 100)
    myList.insertAfter(1, 100)
    myList.append(33)
    print(myList)
    myList.insertAfter(33, 66)

    print(myList)

  


    
