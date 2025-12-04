from veiculos import Veiculo
class Moto(Veiculo):
    def __init__(self, id, marca: str, modelo: str, ano: int, km_atual: float, cilindrada: int):
        super().__init__(id,marca, modelo, ano, km_atual)
        self.cilindrada = cilindrada

   
    def calcular_custo_manutencao(self) -> float:
        custo_base = 300.00
        bonus_cilindrada = self.cilindrada * 0.5
        return custo_base + bonus_cilindrada
    
    def exibir(self):
        super().exibir()
        print(f"cilindrada: {self.cilindrada}")
    
    def pega(self):
     dados = super().pega()       # pega tudo da classe Veiculo
     dados["Cilindradas"] = self.cilindrada
     return dados


    
