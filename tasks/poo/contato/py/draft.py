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