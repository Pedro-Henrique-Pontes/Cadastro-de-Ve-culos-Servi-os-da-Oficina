from veiculos import Veiculo
class Carro(Veiculo):
    def __init__(self,id, marca: str, modelo: str, ano: int, km_atual: float, num_portas: int):
        super().__init__(id,marca, modelo, ano, km_atual)
        self.num_portas = num_portas

    def calcular_custo_manutencao(self) -> float:
        custo_base = 500.00
        penalidade_km = (self.km_atual / 50000) * 100
        return custo_base + penalidade_km
    
    def exibir(self):
        super().exibir()  
        print(f"Número de portas: {self.num_portas}")
  
    def pega(self):
     dados = super().pega()       # pega tudo da classe Veiculo
     dados["Número de portas"] = self.num_portas
     return dados
