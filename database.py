import sqlite3


class BancoDeDados:
    """Classe que representa o banco de dados (database) da aplicação"""

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL
            );
            """)

        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def inserir_cliente(self, nome, cpf, email):
        """Insere cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)

            self.conexao.commit()

        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')

    def buscar_cliente(self, cpf):
        '''Busca um cliente pelo cpf'''
        try:
            cursor = self.conexao.cursor()
            # obtem todos os dados
            cursor.execute("""SELECT * FROM clientes;""")
            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print ('Cliente %s encontrado.' % linha[1])
                    break
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')

    def remover_cliente(self, cpf):
        """Metodo pedido como actividade na aula 94, secção 6, SQLite3"""
        """recomendações em:
            https://docs.python.org/3.4/library/sqlite3.html?highlight=sqlite#module-sqlite3"""
        query = """DELETE FROM clientes WHERE cpf=?;"""
        l_cpf = (cpf,)
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute(query, l_cpf)
            except sqlite3.IntegrityError:
                print('O cpf %s não existe!' % cpf)

            self.conexao.commit()
            print('Cliente com cpf=%s removido' %cpf)

        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')

    def buscar_email(self, email):
        """Metodo pedido como actividade na aula 94, secção 6, SQLite3"""
        """recomendações em:
            https: // docs.python.org / 3.4 / library / sqlite3.html?highlight = sqlite  # module-sqlite3"""
        query = """SELECT * FROM clientes WHERE email=?"""
        l_email = (email,)
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query, l_email)
            resultado = cursor.fetchall()
            print("Resultado com "+str(len(resultado))+" linhas")
            for linha in resultado:
                if linha[3] == email:
                    return True
                else:
                    return "Não encontrado"
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')

    def mostrar_todos(self):
        """Metodo auxiliar para listar todos os elementos da base de dados"""
        query = """SELECT * FROM clientes"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            print('\nLista de registos:')
            for registo in cursor.fetchall():
                #print(registo)
                print('ID: {:2d} | Nome: {:8s} | CPF: {:9s} | E-mail: {}'.format(registo[0], registo[1], registo[2], registo[3]))
            print('\n')
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')