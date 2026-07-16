class Pokemon:
    # Construtor => __init__
    def __init__(self, nome: str, tipo: str):
        # Propriedades
        self.nome = nome
        self.tipo = tipo

    # Funções
    def apresentar_dados(self):
        print(f"""Pokemon: {self.nome}
Tipo: {self.tipo}
""")


# Orientação a objetos
def exemplo_pokedex():
    # Objeto chamado charizard que é instanciado da classe Pokemon
    charizard = Pokemon("Charizard", "Fogo")
    bulbasaur = Pokemon("Bulbasaur", "Planta")

    charizard.apresentar_dados()
    bulbasaur.apresentar_dados()

# exemplo_pokedex()