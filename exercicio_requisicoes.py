from rich.console import Console
from rich.table import Table
import requests
import questionary

url_base = "https://api.franciscosensaulas.com"

def cadastrar_empresa():
    url = f"{url_base}/api/v1/empresa"
    pedir_nome_empresa: str = questionary.text("Digite o nome da empresa").ask()
    pedir_cnpj: str = questionary.text("Digite o CNPJ da empresa").ask()

    empresa = {
        "nome": pedir_nome_empresa,
        "cnpj": pedir_cnpj
    }

    resposta = requests.post(url, json=empresa)
    if resposta.status_code == 201:
        print("Empresa cadastrada com sucesso")
    else:
        print("Não foi possível cadastrar a empresa")


def consultar_empresa():
    url = f"{url_base}/api/v1/empresa"

    resposta = requests.get(url)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Nome da Empresa")
    table.add_column("Cnpj")

    empresas = resposta.json()

    for empresa in empresas:
        table.add_row(str(empresa["id"]), empresa["nome"])

    console.print(table)

def apagar_empresa():
    id = int(questionary.text("Digite o id da empresa que voce deseja apagar: ").ask())
    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.delete(url)

    if resposta.status_code == 204: 
        print("Empresa apagada com sucesso")
    elif resposta.status_code == 404:
        print("Não foi possivel encontrar a Empresa com este codigo")
    else: 
        print("Não foi possivel apagar a Empresa")

apagar_empresa()
