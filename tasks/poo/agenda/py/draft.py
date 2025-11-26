class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        if not self.id or not self.number:
            return False
        if any(c.isalpha() for c in self.number):
            return False
        return True
    
    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str, fone: list[Fone] = []):
        self.fone = fone
        self.name = name
        self.fav: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if not fone.isValid():
            print("fail: invalid number")
            return
        self.fone.append(fone)
        

    def rmFone(self, index: int):
        self.fone.pop(index)

    def toggleFav(self):
        if self.fav == False:
            self.fav = True
            return
        else:
            self.fav = False

    def isFav(self) -> bool:
        if self.fav == True:
            return True
        else:
            return False
        
    def getFones(self):
        return self.fone
    
    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name

    def __str__(self):
        fone = ", ".join([str(x) for x in self.fone])
        if self.fav == True:
            return f"@ {self.name} [{fone}]"
        else:
            return f"- {self.name} [{fone}]"
        
class Agenda:
    def __init__(self, contacts: list[Contact]):
        self.contact = contacts

    def addContato(self, name: str, fone: list[Fone]):
        contato = Contact(name, fone)
        self.contact.append(contato)

def main():
    agenda = Agenda()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
main()
