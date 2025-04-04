class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022)

# Exibindo os dados do carro
print(meu_carro.exibir_dados())
