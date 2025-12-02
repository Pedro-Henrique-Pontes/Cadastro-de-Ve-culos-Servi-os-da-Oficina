class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, km_atual: float, cilindrada: int):
        super().__init__(marca, modelo, ano, km_atual)
        self.cilindrada = cilindrada

   
    def calcular_custo_manutencao(self) -> float:
        custo_base = 300.00
        bonus_cilindrada = self.cilindrada * 0.5
        return custo_base + bonus_cilindrada