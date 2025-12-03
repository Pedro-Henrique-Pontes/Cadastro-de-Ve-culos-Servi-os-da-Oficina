class Oficina:  

    def __init__(self):
         
        self.id=id
        self.Nome = None
        self.Valor = None
        self.Historic= []

    
    def Registrar(self,id,Nome,Valor):

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

        self.Historic.append({
                    "Id": self.id,
                    "Servico": self.Nome,
                    "Valor": self.Valor
                })

        

    def Historico(self,id):
        if self.Historic is None:
                return None
            
        for item in self.Historic:
            if item.get("Id") == id:
                print(item)
    
    def Total(self,id):

        total_servico=0

        if self.Historic is None:
                return None
            
        for item in self.Historic:
            if item.get("Id") == id:
                total_servico+=item["Valor"]

        print("total em serviço:",total_servico)



p1 = Oficina()

p1.Registrar(1,"manutencao",230)
p1.Registrar(1,"manutencao",230)
p1.Registrar(1,"manutencao",230)

p1.Historico(1)
p1.Total(1)

#{'Id': 1, 'Servico': 'manutencao', 'Valor': 230}
#{'Id': 1, 'Servico': 'manutencao', 'Valor': 230}
#{'Id': 1, 'Servico': 'manutencao', 'Valor': 230}
#total em serviço: 690
