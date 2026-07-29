def exemplo_sem_tratamento():
    print("Divisão: ", 10 / 0)
    print("Mensagem depois da Divisão")
    # Lança a excessão: ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10 / 0)
    except ZeroDivisionError:
        print("Não é possivel dividir um numero por zero.")

    print("O programa continuou normalmente")


def exemplo_com_tratamento_conversao():
    numero_digitado: str = "dois"
    try:
        # converter de str para int
        numero: int = int(numero_digitado)
        print("Número digitado: " , numero)
    except ValueError:
        print("Texto digitado não é um número válido")
        # print("Não foi possível converter o número para inteiro")
    print("Acabou")


def exemplo_com_multiplos_tratamentos():
    numero1_digitado = "28"
    numero2_digitado = "9"

    try:
        resultado: int = int(numero1_digitado) / int(numero2_digitado)
        print("Resultado: ", resultado)
    except ZeroDivisionError:
        print("Erro: Não é possivel dividir por zero")
    except ValueError:
        print("Erro: os valores precisam ser numeros")

    print("Obrigado por utilizar nosso sistema")    


def exemplo_mensagem_erro():
    try:
        aluno = {"nome": "pedro", "nota1": 9.75}
        media_aluno = aluno["media"]
        print(media_aluno)
    except KeyError as erro: # 'as' serve para pegar a variavel do erro que ocorreu
        print("Mensagem de erro tentar acessar a chave: " , erro)
# Ponto de  entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    exemplo_mensagem_erro()
    