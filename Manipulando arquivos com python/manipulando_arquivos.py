# Trabalhando com arquivos

# retirando os ips repetidos no arquivo ips.txt
lista = []

with open("ips.txt", "r") as ips:
    for linha in ips:
        if not linha in lista:
            lista.append(linha.replace("\n",""))
        print(f"rejeitado {linha}")

with open("ips-unicos.txt", "a") as ips_unicos:
    for ips in lista:
        ips_unicos.write(ips+"\n")

# separando aprovados e reprovados de notas.txt e gerando txt
lista = []

with open("notas.txt", "r") as boletim:
    for linha in boletim:
        separando = linha.split(",")
        nota1 = separando[2]
        nota2 = separando[3]
        nota3 = separando[4]
        nota4 = separando[5].replace("\n","")
        media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4
        print(media)
        if media >=6:
            with open("aprovados.txt","a") as aprovados:
                aprovados.write(f"{separando[0]},{separando[1]},{media} \n")
        else:
            with open("reprovados.txt", "a") as reprovados:
                reprovados.write(f"{separando[0]},{separando[1]},{media} \n")

# encontrando o prato mais pedido
lista = []
contagem = {}
with open("foods.txt", "r") as pedidos:
    for linha in pedidos:
        separando = linha.split(",")
        lista.append(separando[2].replace("\n",""))
    for x in (lista):
        if x in contagem:
            contagem[x] +=1
        else:
            contagem[x] = 1
    favorito = max(contagem.values())
    for x,y in contagem.items():
        if y == favorito:
            print(f"O prato mais pedido foi {x}, {y} vezes")

