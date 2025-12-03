class fone:
    def __init__(self, id : str, number: str):
        self.id = id
        self.number = number 

    def __str__(self ):
        return f"{self.id}:{self.number}"

    def getid(self) -> str:
        return self.id

    def getnumber(self) -> str:
        return self.number

    def isvalid(self) -> bool:
        validos = "0123456789()+-."
        for c in self.number:
            if c not in validos:
                return False
        return True

#------------------------------------------------------------------

class Contato:
    def __init__(self, nome:str):
        self.nome = nome
        self.fones: list[fone] = []
        self.favorito = False

    def __str__(self):
        sla = "@" if self.favorito else "-"
        fones_str = ", ".join(str(f) for f in self.fones)

        return f"{sla} {self.nome} [{fones_str}]"

    def addfone(self, id:str, number:str):
        sla = fone(id, number)
        if sla.isvalid():
            self.fones.append(sla)
            return True
        else:
            print("erro")
            return False

    def rmfone(self, index:int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("burro")

    def tooglefavorited(self):
        self.favorito = not self.favorito

    def isfavorite(self) -> bool:
        return self.favorito

    def getnome(self) -> str:
        return self.nome

    def getfones(self) -> list:
        return self.fones

    def setnome(self, nome:str):
        self.nome = nome

#-------------------------------------------------------------

class Agenda:
    def __init__(self):
        self.contatos: list[Contato] = []

    def __str__(self):
        return "\n".join(str(c) for c in self.contatos)

    def findposbyname(self, nome:str) -> int:
        for i, c in enumerate(self.contatos):
            if c.getnome()== nome:
                return i
        return -1

    def addcontato(self, nome:str, fones: list[fone]):
        pos = self.findposbyname(nome)
        if pos != -1:
            contato = self.contatos[pos]
            for f in fones:
                if f.isvalid():
                    contato.addfone(f.id, f.number)
            return
        novo = Contato(nome)
        for f in fones:
            if f.isvalid():
                novo.addfone(f.id, f.number)
        self.contatos.append(novo)
        self.contatos.sort(key=lambda c: c.getnome())

    def getcontato(self, nome:str) -> Contato|None:
        pos = self.findposbyname(name)
        if pos != -1:
            return self.contatos[pos]
        return None

    def rmcontato(self, nome:str):
        pos = self.findposbyname(nome)
        if pos != -1:
            self.contatos.pop(pos)

    def search(self, pattern:str) -> list[Contato]:
        res = []
        for c in self.contatos:
            linha = str(c)
            if pattern in linha:
                res.append(c)
        for c in res:
            print(c)
        return res

    def getfavorito(self) -> list[Contato]:
        return [c for c in self.contatos if c.isfavorite()]

    def getcontatos(self) -> list[Contato]:
        return self.contatos
 
def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add" :
            nome = args[1]
            fones = []
            for token in args[2:]:
                id, num = token.split(":")
                fones.append(fone(id, num))
            agenda.addcontato(nome, fones)
        elif args[0] == "rm":
            nome = args[1]
            agenda.rmcontato(nome)
        elif args[0] == "rmFone":
            nome = args[1]
            index = int(args[2])

            pos = agenda.findposbyname(nome)
            if pos != -1:
                agenda.contatos[pos].rmfone(index)
            else:
                print("aaaaa")
        elif args[0] == "search":
            pattern = args[1]
            agenda.search(pattern)
        elif args[0] == "tfav":
            nome = args[1]
            pos = agenda.findposbyname(nome)
            if pos != -1:
                agenda.contatos[pos].tooglefavorited()
        elif args[0] == "favs":
            for c in agenda.getfavorito():
                print(c)

main() 