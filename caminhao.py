class Caminhao(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, km_atual: float, capacidade_carga: float):
        super().__init__(marca, modelo, ano, km_atual)
        self.capacidade_carga = capacidade_carga

    def calcular_custo_manutencao(self) -> float:
        custo_base = 1500.00
        penalidade_carga = self.capacidade_carga * 200
        return custo_base + penalidade_carga