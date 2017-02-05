from database import BancoDeDados

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

    banco.inserir_cliente('Marcos', '1111', 'mcastrosouza@live.com')
    banco.inserir_cliente('Thomas', '2222', 'thomas@gmail.com')
    banco.inserir_cliente('Tony', '3333','tony@server.org')

    banco.mostrar_todos()
    banco.buscar_cliente('2222')

    banco.remover_cliente('2222')
    #Como fazer para avisar que este item já foi removido, e como tal não foi encontrado?
    banco.remover_cliente('2222')

    banco.buscar_cliente('2222')
    banco.mostrar_todos()

    print(banco.buscar_email('mcastrosouza@live.com'))
    #nota: em vez de devolver False, está a devolver None, pois não é encontrada nenhuma correspondência
    print(banco.buscar_email('thomas@gmail.com'))

    banco.desconecta()