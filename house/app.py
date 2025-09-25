import json
import os
'''
# Dados que você quer salvar no JSON (pode ser dict ou list)
bib = []
livros = str(input('Digite o livro que deseja cadastrar: '))
bib.append(livros)


# Cria o arquivo JSON
with open(fr"C:\Users\PICHAU\Desktop\programacao\minhas_aulas\house\bib.json", "a", encoding="utf-8") as f:
    json.dump(bib, f, indent=4, ensure_ascii=False)

print("Arquivo JSON criado com sucesso!")
'''

while True:
    try:
        bib = []
        livros = str(input('Digite o livro que deseja cadastrar: '))
        bib.append(livros)
        with open(fr"C:\Users\PICHAU\Desktop\programacao\minhas_aulas\house\bib.json", "a", encoding="utf-8") as f:
            json.dump(bib, f, indent=4, ensure_ascii=False)
            os.system('cls' if os.name == 'nt' else 'clear')

    except:
        break