class LNode:
    def __init__(self, value = None, n=None):
        self.value = value
        self.n = n

class LinkedList:
    
    def __init__(self, head = None):
        self.head = head
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while i < index:
            if curr == None:
                return -1
            curr = curr.n
            i+=1
        if curr == None:
            return -1
        else:
            return curr.value

    def insertHead(self, val: int) -> None:
        newer = LNode(val, self.head)
        self.head = newer
        

    def insertTail(self, val: int) -> None:
        curr = self.head
        if curr == None:
            self.head = LNode(val)
        else:
            while curr.n != None:
                curr = curr.n
            curr.n = LNode(val)
        

    def remove(self, index: int) -> bool:
        prev = None
        curr = self.head
        i = 0
        if index == 0:
            if curr == None:
                return False
            self.head = curr.n
            return True
        while i < index:
            if curr == None:
                return False
            i += 1
            prev = curr
            curr = curr.n
        if curr == None:
            return False
        prev.n = curr.n
        return True
        
        
        
    def getValues(self) -> List[int]:
        agg = []
        curr = self.head
        while curr != None:
            agg.append(curr.value)
            curr = curr.n
        return agg
