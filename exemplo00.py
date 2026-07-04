def exercicios():

    def exercicio_01_mensagens():
        print("Ola, seja bem vindo")
        print("Estou aprendendo a programar em python")
        print("Pyhton pode ser usado para criar varios tipos de programas")

    def exercicio_02_variaveis():
        nome: str = "Samuel"
        idade: int = 142
        cidade: str = "Blumenau"

        print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}")

    def exercicio_03_input_nome():
        nome: str = input("Digite seu nome: ")

        print(f"Ola, {nome} seja bem vindo ao sistema!")

    def exercicio_04_dados_pessoais():
        nome: str = input("Digite seu nome: ").capitalize()
        bairro: str = input("Digite o seu bairro: ")
        cidade: str = input("Digite a sua cidade: ")

        print(f"{nome} mora no bairro {bairro}, na cidade de {cidade}")

    def exercicio_05_idade_int():
        idade: str = int(input("Digite a sua idade: "))
        bairro: str = input("Digite o seu bairro: ")
        cidade: str = input("Digite a sua cidade: ")

        print(f"Voce tem {idade} anos")

    def exercicio_06_idade_proximo_ano():
        nome: str = input("Digite seu nome: ").capitalize()
        idade: str = int(input("Digite a sua idade: "))

        print(f"{nome}, No proximo ano voce tera {idade + 1}")

    def exercicio_07_dobro_numero_inteiro():
        numero: str = int(input("Digite o numero: "))

        print(f"O dobro de {numero} é {numero*2}")

    def exercicio_08_maioridade():
        idade: str = int(input("Digite a sua idade: "))

        if idade >= 18:
            print("Voce é maior de idade")
        else:
            print("Voce é menor de idade")

    def exercicio_09_numero_positivo():
        numero: str = int(input("Digite o numero: "))

        if numero > 0:
            print("O numero é positivo")
        else:
            print("O numero não é positivo")

    def exercicio_10_entrada_evento():
        nome: str = input("Digite seu nome: ").capitalize()
        idade: str = int(input("Digite a sua idade: "))

        if idade >= 16:
            print(f"{nome} voce pode entrar no evento")
        else:
            print(f"{nome} voce não pode entrar no evento")

    def exercicio_11_verificar_nota():
        nota: float = float(input("Digite a nota: "))

        if nota >= 7:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")

    def exercicio_12_verificar_saldo():
        saldo: float = float(input("Digite o saldo: "))
        valor: float = float(input("Digite o valor: "))

        if valor > saldo:
            print("Saldo insuficiente")
        else:
            print("Compra aprovada")

    def exercicio_13_aprovacao_nota_frequencia():
        nota: float = float(input("Digite a nota: "))
        frequencia: int = int(input("Digite a frequencia: "))

        if nota >= 7 and frequencia >= 75:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")

    def exercicio_14_entrada_gratuita():
        idade: str = int(input("Digite a sua idade: "))

        if idade < 6 or idade >= 60:
            print("Entrada gratuita")
        else:
            print("Entrada paga")

    def exercicio_15_login_simples():
        usuario: str = input("Digite o seu usuario: ")
        senha: str = input("Digite a sua senha: ")

        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso")
        else:
            print("Usuario ou senha incorretos")

    def exercicio_16_mensagem_varias_vezes():
        index: int = 1

        while index < 6:
            print("Estou aprendedo Python")

            index += 1

    def exercicio_17_numeros_pares():
        # faltando no arquivo original - preencher aqui
        pass

    def exercicio_18_repetir_mensagem():
        mensagem: str = str(input("Digite a mensagem"))
        vezes: int = int(input("Digite o numero de repetições"))

        while vezes > 0:
            print(mensagem)

            vezes -= 1

    def exercicio_19_somar_1_ate_n():
        numero: int = int(input("Digite um número: "))
        contador: int = 1
        soma: int = 0

        while contador <= numero:
            soma = soma + contador
            contador += 1

        print(f"A soma é {soma}")

    def exercicio_20_senha_while():
        senha: str = str(input("Digite a senha"))

        while senha != "1234":
            senha = input("Senha incorreta, digite novamente")
        print("Senha correta")

    def exercicio_22_tabuada_while():
        i: int = 0
        numero_tabuada: int = int(input("Digite um numero para fazer tabuada: "))

        while i <= 10:
            tabuada: int = numero_tabuada * i
            print(f"{numero_tabuada} x {i} = {tabuada}")
            i += 1


    def exercicio_23():
        numero: int = int(input("Digite um numero: "))
        soma: int = 0

        while numero != 0:
            soma = soma + numero
            numero: int = int(input("Digite um numero: "))
        print(soma)

    def exercicio_24():
        numero: int = int(input("Digite um numero: "))
        positivos: int = 0

        while numero != 0: 
            if numero > 0:
                positivos += 1
                numero: int = int(input("Digite um numero: "))
            elif numero < 0:
                numero: int = int(input("Digite um numero: "))
        print(positivos)
    
    def exercicio_25():
        numero_maior: int = 0
        i: int = 0

        while i < 5:
            numero: int = int(input("Digite um numero: "))
            if numero > numero_maior:
                numero_maior = numero
            i += 1

        print(numero_maior)
        

    def exercicio_26():
        media: int = 0
        soma: int = 0
        i: int = 1

        while i <= 4:
            nota: float = float(input(f"Digite a {i} nota: "))
            soma = soma + nota
            i += 1

        media = soma / (i - 1)
        print(media)

    def exercicio_27():
        senha_correta: int = int(input("Digite sua senha: "))
        i: int = 1

        while i <= 3:
            pedir_senha: int = int(input("Digite sua senha para ter acesso: "))

            if pedir_senha != senha_correta:
                print(f"Acesso bloqueado!\nVoce tem {3 - i} tentantivas restantes.")
            else:
                print("Acesso permitido!")
            i += 1
    
    def exercicio_28():
        idade: int = int(input("Digite sua idade:"))

        while idade > 120 or idade < 0:
            idade: int = int(input("Idade invalida. Digite-a novamente: "))

        print("Idade cadastrada com sucesso!")

    def exercicio_29():
        numero_secreto: int = 9
        pedir_numero: int = 0

        while pedir_numero != numero_secreto:
            pedir_numero: int = int(input("Digite um numero: "))
            if pedir_numero < numero_secreto:
                print("Numero menor que numero secret")
                pedir_numero: int = int(input("Digite um numero: "))
            elif pedir_numero > numero_secreto:
                print("numero maior que o numero secret")
                pedir_numero: int = int(input("Digite um numero: "))
            else:
                print("Numeros iguais")
    
    def exercicio_30():
        menu: int = int(input(f""" 1 - Somar 
2 - Subtrair
3 - multiplicar
0 - Sair """))

        while menu != 0:
            if menu == 1:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))
            
                soma = numero1 + numero2

                print(soma)

                menu: int = int(input(f""" 1 - Somar 
2 - Subtrair
3 - multiplicar
0 - Sair """))

            if menu == 2:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))

                subtrair = numero1 - numero2

                print(subtrair)

                menu: int = int(input(f""" 1 - Somar 
2 - Subtrair
3 - multiplicar
0 - Sair """))

            if menu == 3:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))

                multiplicar = numero1 * numero2

                print(multiplicar)

                menu: int = int(input(f""" 1 - Somar 
2 - Subtrair
3 - multiplicar
0 - Sair """))

                


    def exercicio_31():
        lado1: int = int(input("Digite o primeiro lado do triangulo: "))
        lado2: int = int(input("Digite o segundo lado do triangulo: "))
        lado3: int = int(input("Digite o terceiro lado do triangulo: "))

        opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n"))

        while opcao != 0:
            if opcao == 1:
                equilatero = lado1 == lado2 == lado3
                if equilatero == True:
                    print("Equilatero")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n "))
                else:
                    print("Não é equilatero")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n "))
            
            if opcao == 2:
                escaleno = lado1 != lado2 != lado3
                if escaleno == True:
                    print("Escaleno")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n "))
                else:
                    print("Não é escaleno")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n"))

            if opcao == 3:
                isoceles = lado1 != lado2 or lado2 != lado3 or lado1 != lado3
                if isoceles == True:
                    print("isoceles")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n "))
                else:
                    print("Não é isoceles")
                    opcao: int = int(input(" 1 - Equilatero\n2 - Escaleno\n3 - Isóceles\n 0 - Sair \n"))



    exercicio_31()

            


            
            

exercicios()
    