from datetime import datetime
from pathlib import Path

def exemplo_tratar_criacao_diretorio():
    try:
        caminho_diretorio = Path("relatorios")
        caminho_diretorio.mkdir()
        print("Criado com sucesso")
    except FileExistsError:
        print("Diretorio já existe")
    finally:
        mensagem = input("Digite uma mensagem para salvar no arquivo: ")

        caminho_arquivo = caminho_diretorio / "relatorio-2026-07-29.txt"
        with open(caminho_arquivo, "a", encoding="UTF-8") as f:
            data_hora_atual = datetime.now()
            f.write(str(data_hora_atual)+ " " + mensagem + " \n")
            print("Arquivo gerado")

if __name__ == "__main__":
    exemplo_tratar_criacao_diretorio()