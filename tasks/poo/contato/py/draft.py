class Fone:
    def __init__(self, id:  str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        if not self.id or not self.number:
            print("fail: invalid number")
            return  False
        return True
    
    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str):
        self.name = name
        self.fone: list[Fone] | None = None
        self.favorited: bool = False

    def addFone(self, id: str, number: str):
        self.fone.append(id, number)

    def getFone(self):
        return self.fone
    
    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name

    def rmFone(self, index: int):
        self.fone.pop(index)

    def toggleFav(self):
        if self.favorited == False:
            self.favorited = True
            return
        if self.favorited == True:
            self.favorited = False
            return
        
    def isFav(self) -> bool:
        if self.favorited == True:
            return True
        else:
            return False
