import json
biblioeteca = {}
class Biblioeteca:
    def __init__(self, nome, autor, genero):
        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    def cadastrar(self):
        
        with open("house/bib.json", "r", encoding="utf-8") as f:
                biblioteca =dict(json.load(f))
                biblioteca["livros"].append({
            "nome": self.nome,
            "autor": self.autor,
            "genero": self.genero
        })
                
        with open("house/bib.json", "w", encoding="utf-8") as f:
            json.dump(biblioteca, f, ensure_ascii=False, indent=4)
        
        print(f"O nome do livro é : {self.nome}")
        print(f"O autor do livro é : {self.autor}")
        print(f"O gênero do livro é : {self.genero}")


  
def deletar():  
    livro = input("Digite o livro que deseja remover: ")
    if livro in biblioeteca:
        del biblioeteca[livro]
        print('Livro deletado com sucesso!')
    else:
        print("Esse livro não esta na biblioteca!")




def menu():
    print()
    print(30*'-', "MENU", 30*"-")
    print("OPÇÃO 1 --  CADASTRAR")
    print("OPÇÃO 3 --  DELETAR")
    print("OPÇÃO 4 --  SAIR")
    print()



def sair():
    exit()
while True:
    menu()
    opcao = input("Digite uma opção: ")
    match opcao:
        case '1' :
            nome = str(input("Digite o nome do livro: "))
            autor = str(input("Digite o nome do autor: "))
            genero = str(input("Digite o gênero: "))
            
            # Cria o objeto e cadastra
            livro = Biblioeteca(nome, autor, genero)
            livro.cadastrar()
        case '3':
            deletar()

        case '4' :
            sair()
