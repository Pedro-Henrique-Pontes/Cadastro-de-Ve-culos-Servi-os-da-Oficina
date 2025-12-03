class Oficina:
    def __init__(self, Nome, Valor):

        if not isinstance(Nome, str) or Nome.strip() == "":
            raise ValueError("Nome inválido: deve ser texto não vazio.")

        if not isinstance(valor, float):
            raise TypeError("o valor deve ser um numero.")

        if valor < 0 :
            raise ValueError("valor deve ser positivo.")

        self.Nome = Nome
        self.Valor = valor
      

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
