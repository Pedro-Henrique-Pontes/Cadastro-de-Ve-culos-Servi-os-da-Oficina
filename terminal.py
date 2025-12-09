from veiculos import Veiculo
from oficina import Oficina
from carro import Carro
from moto import Moto
from caminhao import Caminhao



def main():

    p=[]
    o=[]
    c=0

    while True:
        a = str(input(">")).split()
        cmd = a[0].upper()

        if cmd == "AJUDA" and len(a) == 1:
            print("""
                | Comando    | Descrição                                               | Uso                                                   | Validações / Exceções                                                                 |
                |------------|---------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------|
                | CADASTRAR  | Registra um novo veículo no sistema.                    | CADASTRAR <tipo> <marca> <modelo> <ano> <km> <atrib>  | Tipo inválido; ano fora de faixa; km negativo; atributo específico inválido            |
                | LISTAR     | Exibe todos os veículos cadastrados.                    | LISTAR                                                | Nenhum veículo cadastrado                                                              |
                | DETALHES   | Mostra informações completas de um veículo específico.  | DETALHES <id>                                         | ID inexistente; formato incorreto                                                     |
                | CUSTO      | Calcula custo estimado de manutenção (lógica por tipo). | CUSTO <id>                                            | ID inexistente; veículo não encontrado                                                 |
                | REGISTRAR  | Registra um serviço realizado em um veículo.            | REGISTRAR <id> <servico> <valor>                      | ID inexistente; valor negativo; serviço vazio                                          |
                | HISTORICO  | Exibe serviços realizados em um veículo.                | HISTORICO <id>                                        | ID inexistente; nenhum serviço registrado                                              |
                | TOTAL      | Calcula valor total gasto em serviços de um veículo.    | TOTAL <id>                                            | ID inexistente; nenhum serviço registrado                                              |
                | SAIR       | Encerra o programa.                                     | SAIR                                                  | Nenhuma exceção                                                                        |
            """)

        elif cmd == "CADASTRAR":

            if len(a) != 7:
                    # Usando a mensagem que você pediu:
                    print("Formato incorreto. Use: CADASTRAR <tipo> <marca> <modelo> <ano> <km> <atrib_especifico>")
                    continue
            else:
             
                if a[1].upper() == "CARRO":

                    c+=1
                    p.append(Carro(c,a[2],a[3],int(a[4]),float(a[5]),float(a[6])))
                    print("Registro de Carro:",c)

                if a[1].upper() == "CAMINHAO":
                     
                     c+=1
                     p.append(Caminhao(c,a[2],a[3],int(a[4]),float(a[5]),float(a[6])))
                     print("Registro de Caminhao:",c)

                if a[1].upper() == "MOTO":
                     
                     c+=1
                     p.append(Moto(c,a[2],a[3],int(a[4]),float(a[5]),float(a[6])))
                     print("Registro de Moto:",c)
            
             
            
        elif cmd == "LISTAR":

            for x in p :

                x.exibir()
            
        elif cmd == "DETALHES":

            if len(a) < 2:
                print("Formato incorreto. Use: DETALHES <id>")

                continue

            else:

             for x in p :

                y=x.pega()

                if y["Id"]==int(a[1]):
                 print(y)
            
        elif cmd == "CUSTO":

            if len(a) < 2:
                print("Formato incorreto. Use: CUSTO <id>")
                continue
            
            else:

             for x in p :

                y=x.pega()

                if y["Id"]==int(a[1]):
                 print("Custo Estimado:",x.calcular_custo_manutencao())

        elif cmd == "REGISTRAR":
         
            if len(a) != 4:
                # Usando a mensagem que você pediu:
                print("Formato incorreto. Use: Registrar <ID> <Servico> <Valor>")
            
            else:
                
                for h in p:
                
                    if h.id_existe(int(a[1]))==True:
                        o.append(Oficina(int(a[1]),a[2],float(a[3])))
                        print("Registro de servico:",a[1])


        elif cmd == "HISTORICO": 

            if len(a) != 2:
                # Usando a mensagem que você pediu:
                print("Formato incorreto. Use: Historico <ID> ")

            else:
                
                for l in o:

                    r=l.pegaO()

                    if r["Id"]==int(a[1]):
                        print(r["Servico"],":",r["Valor"])

        elif cmd == "TOTAL":

            valor=0

            if len(a) != 2:
                # Usando a mensagem que você pediu:
                print("Formato incorreto. Use: TOTAL <ID> ")

            else:
                
                for l in o:

                    r=l.pegaO()

                    if r["Id"]==int(a[1]):
                        valor+=r['Valor']

                print("Valor total =",valor)


        elif cmd == "SAIR":
            break
        else:
            print("Comando Inválido, digite AJUDA se precisar de auxílio")

main()
