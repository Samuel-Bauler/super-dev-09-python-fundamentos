def exercicio01():
    for i in range(0, 5):
        print("Bem vindo!")
    
def exercicio02():
    for i in range(15 , 30):
        print(i + 1)

def exercicio03():
    pedir_numero: int = int(input("Qual numero voce quer a tabuada?"))
    for i in range(1, 11):
        tabuada: int = pedir_numero * i

        print(f"{pedir_numero} x {i} = {tabuada}")

def exercicio04():
    soma: int = 0
    for i in range(1, 6):
        pedir_numeros: int = int(input(f"Digite o {i}º número: "))
        soma: int  = soma + pedir_numeros

    print(soma)

def exercicio05():
    nomes = []
    nomes.append("Samuel")
    nomes.append("Francisco")
    nomes.append("Mateus com H")
    nomes.append("Victor sem C")

    print(nomes[0])
    print(nomes[1])
    print(nomes[2])
    print(nomes[3])
    
def exercicio06():
    frutas = []
    frutas.append(input("Digite o nome da primeira fruta: "))
    frutas.append(input("Digite o nome da segunda fruta: "))
    frutas.append(input("Digite o nome da terceira fruta: "))

    print(frutas[0])
    print(frutas[1])
    print(frutas[2])

def exercicio07():
    numeros = []
    numeros.append(int(input("Digite o primeiro numero: ")))
    numeros.append(int(input("Digite o segundo numero: ")))
    numeros.append(int(input("Digite o terceido numero: ")))
    numeros.append(int(input("Digite o quarto numero: ")))

    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])

def exercicio08():
    notas = []
    notas.append(int(input("Digite o primeiro nota: ")))
    notas.append(int(input("Digite o segundo nota: ")))
    notas.append(int(input("Digite o terceido nota: ")))
    notas.append(int(input("Digite o quarto nota: ")))

    print(f"\nPrimeira nota digitada: {notas[0]}\n ")

    print(f"Ultima nota digitada: {notas[3]:}\n ")

    notas.remove(notas[2])
    print("Terceira nota excluida")

    print("Tamanho da lista: " , len(notas))

    media: int = (notas[0] + notas[1] + notas[2]) / 3

    print("\nVetor final: \n")
    print(notas[0])
    print(notas[1])
    print(notas[2])

    print(f"\nMédia final\n")
    print(media)
    

exercicio08()

