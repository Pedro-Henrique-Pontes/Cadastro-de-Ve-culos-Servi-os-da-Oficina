class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, km_atual: float, num_portas: int):
        super().__init__(marca, modelo, ano, km_atual)
        self.num_portas = num_portas

     def calcular_custo_manutencao(self) -> float:
        custo_base = 500.00
        penalidade_km = (self.km_atual / 50000) * 100
        return custo_base + penalidade_km
