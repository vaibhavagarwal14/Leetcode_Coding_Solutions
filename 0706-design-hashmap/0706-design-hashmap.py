class MyHashMap:

    def __init__(self):
        self.lst=[]
        self.l=0

    def put(self, key: int, value: int) -> None:
        f=0
        for i in self.lst:
            if i[0]==key:
                i[1]=value
                f=1
                break
        if f==0:
            self.lst.append([key,value])
        self.l+=1

    def get(self, key: int) -> int:
        for i in self.lst:
            if i[0]==key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.lst)):
            if self.lst[i][0]==key:
                del self.lst[i]
                self.l-=1
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)