def main():

    while True:
        a = str(input("")).split()
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

            cadastrar(a) 
            
        elif cmd == "LISTAR":
            sistema.listar()
            
        elif cmd == "DETALHES":
            if len(a) < 2:
                print("Formato incorreto. Use: DETALHES <id>")
                continue
            sistema.detalhes(a[1])
            
        elif cmd == "CUSTO":
            if len(a) < 2:
                print("Formato incorreto. Use: CUSTO <id>")
                continue
            sistema.custo(a[1])
            
        elif cmd == "SAIR":
            break
        else:
            print("Comando Inválido, digite AJUDA se precisar de auxílio")

main()