def exemplo_sem_erro():
    try:
        resultado = 10 / 2
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero " )
    finally:
        print("FINALLY: executei mesmo sem erro")


def exemplo_com_erro():
    try: 
        resultado = 10 / 0
        print("Resultado: " , resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    finally:
        print("FINALLY: executei mesmo com erro" )

if __name__ == "__main__":
    exemplo_com_erro()
    # exemplo_com_erro()