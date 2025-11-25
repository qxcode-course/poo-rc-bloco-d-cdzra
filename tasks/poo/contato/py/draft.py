class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        if not self.id or not self.number:
            return False
        return True
    
    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str):
        self.fone: list[Fone] = []
        self.name = name
        self.fav: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
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
        
def main():
    contatos = Contact("")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(contatos)
        elif args[0] == "init":
            name = args[1]
            contatos.setName(name)
        elif args[0] == "add":
            id = args[1]
            number = args[2]
            contatos.addFone(id, number)
        elif args[0] == "rm":
            index = int(args[1])
            contatos.rmFone(index)
main()
