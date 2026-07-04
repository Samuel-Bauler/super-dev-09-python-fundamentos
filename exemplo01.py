import os
import time

def exemplo_string():
    # declarando uma variavel do tipo string
    nome_livro_comeco: str = "harry potter"
    nome_livro_final: str = "As reliquias da morte"
    # declarando uma string e armazendo a concatenacao
    # title => Pascal Case
    # upper => UPPER CASA
    # lower => lower case
    # capitalize => Abacate com pera e limão
    nome_livro: str = nome_livro_comeco.title() + " " + nome_livro_final.upper()
    print("Livro das filhas da Miranda: ", nome_livro)


def primeiro_exemplo():
    print("Olá Mundo")
    fruta: str = "Abacate"
    carro: str = "Corsa"
    quantidade_fruta: int = 6
    preco_unitario_fruta: float = 2.53
    print("Fruta:", fruta)
    print("Quantidade: ", quantidade_fruta)
    print("Preço unitario: ", preco_unitario_fruta)
    print("Preço total:", quantidade_fruta * preco_unitario_fruta)
    print("O carro", carro, " comprou a fruta: ", fruta)


def exemplo_solicitar_dados():
    # convertendo para letra maiuscula o que o usuario digitou 
    # removendo os espaços do começo e do fim
    console: str = input("Digite o nome do console: [XBOX/PS5]").upper().strip()
    quantidade: int = int(input("Digite a quantidade: "))

    preco: float = 0
    if console == "XBOX":
        preco = 6696.0
    # elif é 'else if'
    elif console == "PS5":
        preco = 4277.07
    else:
        print("Console invalido")
        return
    
    print("Preço:", preco)
    print("Quantidade: ", quantidade)
    print("Total: ", preco * quantidade)


def exemplo_if_aluno():
    # float(....)é a forma que convertemos de string para float
    nota1: float = float(input("Digite a nota 1: "))
    nota2: float = float(input("Digite a nota 2: "))
    nota3: float = float(input("Digite a nota 3: "))

    media: float = (nota1 + nota2 + nota3) / 3

    # bool é boolean (True ou false)
    aprovado: bool = False

    if media >= 6 and media <= 10:
        aprovado = True
    else:
        aprovado = False

    print("Média: ", media) 

    if aprovado == True:
        print("Aprovado: sim")
    else:
        print("Aprovado: não")


def exemplo_while():
    def contar_ate_5():
        i = 0 
        # apresentar de 0 até 4 
        while i < 5:
            print(i)
            #i = i + 1 incrementar
            i += 1


    def contagem_regressiva():
        i = 5
        print("Contagem regressiva")
        # apresentar de 5 até 0
        while i >= 0:
            print(i)
            # i = i - 1 Decrementar
            i -= 1


    def solicitar_dados():
        i = 0
        total_mensal_salarios = 0
        while i < 3:
            jogador: str = input("Nome do jogador de futebol: ")
            posicao: str = input("posição do jogador:")
            salario_anual: float = float("Salario anual")

            salario_mensal = salario_anual / 12
            # separator permite mudar o comportamento de como será concatenado os dados no print
            # end permite mudar oque acontece depois que terminou de imprimir no terminal
            print("jogador: ", jogador, "ganha R$", salario_mensal, sep="  ", end="\n\n\n\n")

            total_mensal_salarios = total_mensal_salarios + salario_mensal
            i += 1

    def escrever_arquivo_copa_mundo():
        # criar arquivo CSV com os dados que o usuario digitar
        texto_arquivo = "Time1;Time2;Placar\n"

        i = 0
        while i < 3:
            time1: str = input("Time 1")
            time1_gols: int = int(input("Gols " + time1 + ": "))

            time2: str = input("Time 2")
            time2_gols: int = int(input("Gols " + time2 + ": "))

            placar = str(time1_gols) + "x" + str(time2_gols)

            # interpolação de string (forma simplificada da linha)
            texto_arquivo += f"{time1};{time2};{placar}"
            print("\n\n\n--------------------------------------------")

            if time1_gols > time2_gols:
                print(f"Resultado: time {time1} ganhou")
            elif time2_gols > time1_gols:
                print(f"Resultado: Time {time2} ganhou")
            else:
                print("Resultado: Empate")

            time.sleep(2)

            limpar_terminal = input("Deseja limpar terminal [y/n]")
            if limpar_terminal == "y":
                os.system("cls")

            i = i + 1

            # criar arquivo em python
            with open("placar.csv", "w", encoding="utf-8") as arquivo:
                arquivo.write(texto_arquivo)
                print("Arquivo 'placar.csv' criado com sucesso")

    escrever_arquivo_copa_mundo()

exemplo_while()
 
