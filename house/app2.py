import json




with open("house/bib.json", "r", encoding="utf-8") as f:
    biblioteca = dict(json.load(f))
livro = {
     "nome" : input("Digite:"),
     "autor" : input("Digite:"),
     "genero" : input("Digite:")

}

biblioteca["livros"].append(livro)
with open("house/bib.json", "w", encoding="utf-8") as f:
     json.dump(biblioteca, f,ensure_ascii=False, indent=4)
print(f" - {livro["nome"]} ({livro["autor"]} / {livro["genero"]})")