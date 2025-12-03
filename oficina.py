class Oficina:
    def __init__(self,id, Nome, Valor ):

        if not isinstance(Nome, str) or Nome.strip() == "":
            raise ValueError("Nome inválido: deve ser texto não vazio.")

        if not isinstance(valor, float):
            raise TypeError("o valor deve ser um numero.")

        if valor < 0 :
            raise ValueError("valor deve ser positivo.")
            
        self.id=id
        self.Nome = Nome
        self.Valor = Valor

        p=[]
        
        p.append({
            "Id": self.Valor,
            "Servico": self.Nome,
            "Valor do servico": self.Valor
        })

        def Historico(self,id):

            for x in p :

                print(x)
      
