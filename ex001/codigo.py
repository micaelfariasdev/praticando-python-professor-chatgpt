
with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo1 = conteudo.split()
conteudo1 = "".join(conteudo1)
cont = 0
for i in conteudo1:
    cont += 1
print(f'O arquivo {arquivo.name} possui {cont} letras')

cont2 = sum(1 for c in conteudo if c.isalpha())
print(f'O arquivo {arquivo.name} possui {cont2} letras.')