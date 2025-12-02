class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, quilometragem):

        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("Marca inválida: deve ser texto não vazio.")

        if not isinstance(modelo, str) or modelo.strip() == "":
            raise ValueError("Modelo inválido: deve ser texto não vazio.")

        if not isinstance(ano_fabricacao, int):
            raise TypeError("Ano de fabricação deve ser inteiro.")

        if ano_fabricacao < 1800 or ano_fabricacao > 2026:
            raise ValueError("Ano deve estar entre 1800 e 2026.")

        if not isinstance(quilometragem, (int, float)):
            raise TypeError("Quilometragem deve ser numérica.")

        if quilometragem < 0:
            raise ValueError("Quilometragem deve ser ≥ 0.")

        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.quilometragem = quilometragem

    def calcular_custo_manutencao(self) -> float:
        #Método genérico.
        raise NotImplementedError("O cálculo do custo de manutenção deve ser implementado na subclasse.")

'''
Victor, vou deixar isso aqui pra n esquecer como fiz:
O critério para calcular o custo estimado de 
manutenção para cada tipo de veículo foi estabelecido com base em características específicas que 
tendem a influenciar os gastos ao longo do tempo. Para o Carro, o custo considera uma base fixa somada 
a uma penalidade pela alta quilometragem km; quanto mais o carro rodou, maior é a estimativa 
de gasto, refletindo o desgaste natural das peças. Já para a Moto, o custo também tem uma base fixa, mas
é incrementado por um bônus proporcional à cilindrada, pois motocicletas de maior cilindrada geralmente
têm componentes mais potentes e, consequentemente, manutenções mais caras. Por fim, para o Caminhão, o
cálculo inclui o custo base mais uma penalidade diretamente relacionada à sua capacidade de carga em 
toneladas, pressupondo que veículos que transportam cargas mais pesadas sofrem um estresse estrutural
maior e demandam manutenções mais robustas.
'''