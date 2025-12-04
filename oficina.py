

class Oficina:  

    def __init__(self,id,Nome,Valor):

        if not isinstance(Nome, str) or Nome.strip() == "":
            raise ValueError("Nome inválido: deve ser texto não vazio.")
        else:
            self.Nome=Nome

        if not isinstance(Valor, (int,float)):
            raise TypeError("o valor deve ser um numero.")
            
        if Valor < 0 :
            raise ValueError("valor deve ser positivo.")
        else:
            
            self.Valor= Valor

        self.id=id
         
        self.id=id
        self.Nome = Nome
        self.Valor = Valor          
    
    def pegaO(self):

        return {'Id': self.id, 'Servico': self.Nome, 'Valor': self.Valor}

    def Total(self,id):

        total_servico=0

        if self.Historic is None:
                return None
            
        for item in self.Historic:
            if item.get("Id") == id:
                total_servico+=item["Valor"]

        print("total em serviço:",total_servico)

