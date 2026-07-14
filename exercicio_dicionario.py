from typing import Dict

def exemplo_revisao():
    celular: Dict[str, str|float|int|bool] = {}
    celular["modelo"] = "Samsung A03"
    celular["Armazenamento"] = 256
    celular["lancado"] = True


    print("celular: ", celular["modelo"])

def exercicio_02():
    aluno: Dict[str, str|int] = {}
    aluno["nome"] = "Mateus Com H"
    aluno["idade"] = 18
    aluno["turma"] = 301
    aluno["curso"] = "Fullstack em Python"

    for key in aluno.keys():
        print(key)

def exercicio_03():
    produto: Dict[str, str|float] = {}

    produto["nome"] = "Retroescavadeira"
    produto["preco"] = 3_000_000
    produto["estoque"] = 132
    produto["categoria"] = "fazedora de buraco"

    for value in produto.values():
        print(value)

def exercicio_04():
    funcionario: Dict[str, str|float] = {}

    funcionario["nome"] = "Rogerio"
    funcionario["cargo"] = "Dono"
    funcionario["salario"] = 10_232_232.87
    funcionario["setor"] = "Administrativo"

    for chave, valor in funcionario.items():
        print(chave, ":" , valor)


def exercicio_05():
    livro: Dict[str, str|int] = {}
    livro["titulo"] = input("Digite o titulo do livro: ")
    livro["autor"] = input("Digite o autor do livro: ")
    livro["ano_publicacao"] = int(input("Digite o ano de publicação: "))
    livro["quantidade_paginas"] = int(input("Digite a quantidade de páginas: "))

    for key, value in livro.items():
        print(key , ":" , value)

def exercicio_06():
    i: int = 1
    jogos = [
        {
            "nome_jogo": "Red Dead Redeption",
            "genero": "RPG",
            "ano_lancamento": 1983,
            "preco": 300
        },
        {
            "nome_jogo": "Good of War",
            "genero": "Simulator",
            "ano_lancamento": 1576,
            "preco": 584.76
        }
    ]
    
    for jogo in jogos:
        print("Jogo" , i)
        for key,value in jogo.items():
            print(f"{key}: {value}")
            
        print("\n")
        i += 1

def exercicio_07():
    apresentar_nomes: str = input("Deseja saber os nomes dos produto: (Y/N)")
    obter_ou_não_nomes: bool = False
    if apresentar_nomes == "Y":
        obter_ou_não_nomes == True
        return obter_nomes_produtos()
    else: 
        obter_ou_não_nomes == False


def obter_nomes_produtos():
    produtos = [
        {
            "nome_produto": "Notebook Dell Inspiron 15",
            "categoria": "Eletrônicos",
            "ano_fabricacao": 2024,
            "preco": 4599.90
        },
        {
            "nome_produto": "Smartphone Samsung Galaxy A56",
            "categoria": "Eletrônicos",
            "ano_fabricacao": 2025,
            "preco": 2199.90
        },
        {
            "nome_produto": "Cafeteira Elétrica Mondial",
            "categoria": "Eletrodomésticos",
            "ano_fabricacao": 2023,
            "preco": 299.90
        },
        {
            "nome_produto": "Bicicleta Aro 29 Caloi",
            "categoria": "Esportes",
            "ano_fabricacao": 2024,
            "preco": 1899.90
        },
        {
            "nome_produto": "Sofá Retrátil 3 Lugares",
            "categoria": "Móveis",
            "ano_fabricacao": 2024,
            "preco": 2599.90
        }
    ]

    for produto in produtos:
        print(produto["nome_produto"])

exercicio_07()






    