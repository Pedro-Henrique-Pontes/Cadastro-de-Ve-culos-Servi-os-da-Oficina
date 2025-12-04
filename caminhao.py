from veiculos import Veiculo
class Caminhao(Veiculo):
    def __init__(self,id, marca: str, modelo: str, ano: int, km_atual: float, capacidade_carga: float):
        super().__init__(id,marca, modelo, ano, km_atual)
        self.capacidade_carga = capacidade_carga
        

    def calcular_custo_manutencao(self) -> float:
        custo_base = 1500.00
        penalidade_carga = self.capacidade_carga * 200
        return custo_base + penalidade_carga
    
    def exibir(self):
        super().exibir()
        print(f"capacidade de carga: {self.capacidade_carga}")

    def pega(self):
     dados = super().pega()       # pega tudo da classe Veiculo
     dados["Carga"] = self.capacidade_carga
     return dados
