def exercicio09():
    nomes = []
    nomes.append("Victor sem C")
    nomes.append("Mateus com H")
    nomes.append("Samuel")
    nomes.append("Francisco")
    nomes.append("Lucas")

    for nome in nomes:
        print(nome)

def exercicio10():
    frutas = []
    for i in range(1, 6):
        frutas.append(str(input(f"Digite a {i} fruta: ")))

    for fruta in frutas:
        print(fruta)

def exercicio11():
    numeros = []
    soma: int = 0
    i: int = 1
    for j in range(1, 6):
        numeros.append(int(input(f"Digite o {j} número: ")))

    print("\nNúmeros digitados:\n")
    for numero in numeros:
        print(f"{i}º = {numero} ")
        i += 1


    for numero in numeros:
        soma = soma + numero
    
    print("\nSoma total: " , soma)

def exercicio12():
    numeros = []
    pares: int = 0
    for i in range(1, 7):
        numeros.append(int(input(f"Digite o {i} número:")))
        
    
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
    
    print("Números pares:" , pares)

def exercicio13():
    notas = []
    soma: int = 0
    for i in range(1,5):
        notas.append(int(input(f"Digite a sua {i} nota: ")))

    for nota in notas:
        soma += nota

    media: float = soma / len(notas)

    print("Notas digitadas: \n")
    for nota in notas:
        print(nota)

    print("média final" , media)

    if media < 6:
        print("Reprovado")
    else:
        print("Aprovado")
    
exercicio13()
    
    