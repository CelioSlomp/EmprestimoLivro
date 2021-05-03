"""Programa de Empréstimo de Livros

Autores:
@Celio Ludwig Slomp
@Igor Zafriel Schmidt
@Pedro Romig de Lima Souza

Turma: Info - 202
"""
import sys
import sqlite3

# É criada uma conexão com o banco de dados "Emprestimo_Livro.db".
conexao = sqlite3.connect("Emprestimo_Livros.db")

# É criado um cursor para poder manipular os itens do banco de dados.
cursor = conexao.cursor()

# Foi utilizado um comando para que caso a tabela já exista, ele ignore
# Porém, caso a tabela não exista, ela seja criada.
cursor.execute("create table if not exists usuarios_cadastrados \
(id integer primary key, nome, cpf, telefone, email, rg, cep, idade)")
cursor.execute("create table if not exists livros_cadastrados \
(id integer primary key, titulo, autor, descricao, isbn, lancamento, situacao)")
cursor.execute("create table if not exists emprestimos_ativos \
(id integer primary key, id_usuario, id_livros, data_validade)")


class Livros:
    """Essa clase representa os livros no mundo real.

    Args:
        titulo (str): O titulo do livro
        autor (str): O nome do autor do livro
        descricao (str): A descrição do livro
        isbn (str): O isbn do livro
        lancamento (str): Data de publicação/lançamento do livro
        situacao (str): A situacao do livro (emprestado ou não)
    """
    def __init__(self, titulo: str, autor: str, descricao: str, isbn: str, 
                            lancamento: str, situacao: str, recuperar: bool):
        """Cadastra/recupera um livro.

        Cadastra um livro da vida real em um banco de dados para poder ter
        um certo controle na biblioteca.
        Ele também recupera os objetos de dentro da lista na classe Biblioteca.

        Args:
            titulo (str): O titulo do livro
            autor (str): O nome do autor do livro
            descricao (str): A descrição do livro
            isbn (str): O isbn do livro
            lancamento (str): Data de publicação/lançamento do livro
            situacao (str): A situacao do livro (emprestado ou não)
        """
        listaitens = []
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao
        self.isbn = isbn
        self.lancamento = lancamento
        self.situacao = situacao
        # Aqui são adicionados os itens à uma lista.
        listaitens.append(titulo)
        listaitens.append(autor)
        listaitens.append(descricao)
        listaitens.append(isbn)
        listaitens.append(lancamento)
        listaitens.append(situacao)
        if recuperar == False:
            # Ao final do execute, está uma lista que contém todos os parâmetros dados acima.
            # Ele apenas irá funcionar caso o parâmetro recuperar seja False, que significa 
            # aonde foi chamado essa classe.
            cursor.execute("insert into livros_cadastrados (id, titulo, autor, descricao,\
            isbn, lancamento, situacao) values (null, ?, ?, ?, ?, ?, ?)", listaitens)


class Emprestimo:
    """Essa classe representa um empréstimo da vida real.

    Essa classe cadastra os empréstimos de livros da biblioteca
    aos usuários que estão cadastrados.
    O usuário pode também alterar a data de validade do empréstimo.

    Args:
        id_usuario (str): O id do usuário que fará o empréstimo.
        id_livros (str): O id do(s) livros que serão emprestados.
        data_validade (str): A data limite para renovar o empréstimo.
        recuperar (bool): Serve para o código ter um controle para as recuperações.
    """
    def __init__(self, id_usuario, id_livros, data_validade, recuperar):
        """Cadastra/recupera um empréstimo.
        
        Esse método cria um objeto utilizando os args.
        Dependendo do parâmetro 'recuperar', ele não salvará no banco de dados.


        Args:
            id_usuario (str): O id do usuário que fará o empréstimo.
            id_livros (str): O id do(s) livros que serão emprestados.
            data_validade (str): A data limite para renovar o empréstimo.
            recuperar (bool): Serve para o código ter um controle para as recuperações.
        """
        listaitens = []
        self.id_usuario = str(id_usuario)
        self.id_livros = str(id_livros)
        self.data_validade = str(data_validade)
        listaitens.append(id_usuario)
        listaitens.append(id_livros)
        listaitens.append(data_validade)
        if recuperar == False:
            # Ao final do execute, está uma lista que contém todos os parâmetros dados acima.
            # Ele apenas irá funcionar caso o parâmetro recuperar seja False, que significa 
            # aonde foi chamado essa classe.
            cursor.execute("insert into emprestimos_ativos (id, id_usuario, id_livros, \
        data_validade) values (null, ?, ?, ?)", listaitens)


class Usuario:
    """Essa classe representa um usuário do mundo real.

    Essa classe cadastra os usuário na lista, e dependendo do caso, no banco de dados.

    Args:
        nome (str): o nome do usuário.
        cpf (str): o cpf do usuário.
        telefone (str): o telefone do usuário.
        email (str): o email do usuário.
        rg (str): o rg do usuário.
        cep (str): o cep do usuário.
        idade (str): a idade do usuário.
        recuperar (bool): Serve para que o código saiba se é pra recuperar os itens
        ou se é para salvar no banco de dados junto.
    """
    def __init__(self, nome, cpf, telefone, email, rg, cep, idade, recuperar):
        """Cadastra/recupera um usuário.

        Esse método cria um objeto para a aplicação do programa.
        Dependendo do parâmetro 'recuperar', ele não salvará no banco de dados.

        Args:
            nome (str): o nome do usuário.
            cpf (str): o cpf do usuário.
            telefone (str): o telefone do usuário.
            email (str): o email do usuário.
            rg (str): o rg do usuário.
            cep (str): o cep do usuário.
            idade (str): a idade do usuário.
            recuperar (bool): Serve para que o código saiba se é pra recuperar os itens
            ou se é para salvar no banco de dados junto.  
        """
        listaitens = []
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.rg = rg
        self.cep = cep
        self.idade = idade
        listaitens.append(nome)
        listaitens.append(cpf)
        listaitens.append(telefone)
        listaitens.append(email)
        listaitens.append(rg)
        listaitens.append(cep)
        listaitens.append(idade)
        if recuperar == False:
            # Ao final do execute, está uma lista que contém todos os parâmetros dados acima.
            # Ele apenas irá funcionar caso o parâmetro recuperar seja False, que significa 
            # aonde foi chamado essa classe.
            cursor.execute("insert into usuarios_cadastrados (id, nome, cpf, telefone, \
            email, rg, cep, idade) values (null, ?, ?, ?, ?, ?, ?, ?)", listaitens)


class Biblioteca:
    """Essa classe representa uma biblioteca da vida real.

    Para ser mais fácil, foi criada essa classe que irá 'gerenciar' todas as outras
    classes, utilizando os métodos abaixo.

    Args:
        lista_usuarios (list): É uma lista que serve para guardar os objetos usuário.
        lista_livros (list): É uma lista que serve para guardar os objetos livro.
        lista_emprestimos (list): É uma lista que serve para guardar os objetos emprestimo.
    """
    def __init__(self):
        """Cria as listas com objetos.

        Esse método cria todas as listas com objetos que será utilizado no programa,
        e também recupera todos os itens que estão no banco de dados para as listas 
        de objetos (citadas abaixo).

        Args:
            lista_usuarios (list): É uma lista que serve para guardar os objetos usuário.
            lista_livros (list): É uma lista que serve para guardar os objetos livro.
            lista_emprestimos (list): É uma lista que serve para guardar os objetos emprestimo.
        """
        self.lista_usuarios = []
        self.lista_livros = []
        self.lista_emprestimos = []
        self.recuperar_livros()
        self.recuperar_usuarios()
        self.recuperar_emprestimos()

    # Usuarios_______________________________________________________________________
    # Usuarios_______________________________________________________________________
    # Usuarios_______________________________________________________________________

    def adicionar_usuario(self):
        """Adiciona um usuário à lista.

        Esse método adiciona as características de um objeto (usuário) ao banco de dados.
        """
        nome = input("Digite o nome do novo usuário: ")
        cpf = input("Digite o cpf do novo usuário: ")
        telefone = input("Digite o telefone do novo usuário: ")
        email = input("Digite o email do novo usuário: ")
        rg = input("Digite o rg do novo usuário: ")
        cep = input("Digite o cep da cidade onde o novo usuário mora: ")
        idade = input("Digite a idade do novo usuuário: ")
        verificador = 0
        # Primeiramente, ele verifica se o cpf do usuário já existe.
        for usuario in self.lista_usuarios:
            if usuario.cpf == cpf:
                verificador = 1
        # Caso ele existe, a variável 'verificador' irá receber '1', fazendo com que
        # ele não vá para o 'else', que irá adicionar o objeto.
        if verificador == 1:
            print("CPF já está sendo usado, tente outra vez.")
            verificador = 0
        else:
            # Adiciona o usuário no banco de dados e na lista de usuários.
            self.lista_usuarios.append(Usuario(nome, cpf, telefone, 
                                                email, rg, cep, idade, False))

    def remover_usuario(self):
        """Remove um usuário

        Esse método remove um usuário do banco de dados do programa utilizando apenas
        o 'id' do usuário.
        """
        id_usuario = []
        id_usuario.append(int(input("Digite o id do usuário que irá deletar: ")))
        cursor.execute("delete from usuarios_cadastrados where id = ?", id_usuario)

    def recuperar_usuarios(self):
        """Recupera os usuários.

        Quando o programa é fechado, as listas perdem aquilo que guardam, então 
        esse método cria todos os objetos para serem apenas adicionados à lista.
        """
        for linha in cursor.execute("select id, nome, cpf, telefone, email, rg,\
                                            cep, idade from usuarios_cadastrados"):
            self.lista_usuarios.append(Usuario(linha[1], linha[2], linha[3], 
                                        linha[4], linha[5], linha[6], linha[7], True))

    # Livros_________________________________________________________________________
    # Livros_________________________________________________________________________
    # Livros_________________________________________________________________________

    def adicionar_livro(self):
        """Adiciona um livro à lista.

        Esse método adiciona as características de um objeto (livro) ao banco de dados.
        """
        titulo = str(input("Digite o título do livro: "))
        autor = str(input("Digite o nome do autor do livro: "))
        descricao = str(input("Digite a descrição do livro: "))
        isbn = input("Digite o isbn do livro: ")
        lancamento = input("Digite a data de publicação do livro(dd/mm/aa): ")
        situacao = "Nao Emprestado"
        verificador = 0

        # Primeiramente ele verifica pelo isbn do livro se ele já existe ou não 
        # para então adicionar à lista e ao banco de dados.
        # Caso o isbn já exista, a variável 'verificador' receberá 1, e não irá
        # para o 'else' que é onde é criado o objeto.
        for livro in self.lista_livros:
            if livro.isbn == isbn:
                verificador = 1
        if verificador == 1:
            print("Este livro já está cadastrado")

        else:
            self.lista_livros.append(Livros(titulo, autor, descricao, isbn, 
                                                lancamento, situacao, False))

    def remover_livro(self):
        """Remove um livro

        Esse método remove um livro (que é especificado pelo id) do banco de dados 
        dados do programa.
        """
        id_livro = []
        id_livro.append(int(input("Digite o id do livro que irá deletar: ")))
        cursor.execute("delete from livros_cadastrados where id = ?", id_livro)

    def recuperar_livros(self):
        """Recupera os livros.

        Quando o programa é fechado, as listas perdem aquilo que guardam, então 
        esse método cria todos os objetos para serem apenas adicionados à lista.
        """
        for linha in cursor.execute("select id, titulo, autor,\
                                    descricao, isbn, lancamento, situacao from livros_cadastrados"):
            self.lista_livros.append(Livros(linha[1], linha[2], linha[3], 
                                        linha[4], linha[5], linha[6], True))

    # Emprestimos___________________________________________________________________
    # Emprestimos___________________________________________________________________
    # Emprestimos___________________________________________________________________

    def adicionar_emprestimo(self):
        """Adiciona um empréstimo.

        Esse método adiciona as características de um objeto (empréstimo) 
        ao banco de dados.
        """
        id_usuario = input("Digite o id do usuário:")
        # Primeiramente é verificado se o usuário existe dentro do banco de dados.
        verific = 0
        for verificacao in cursor.execute("select id from usuarios_cadastrados"):
            valor = str(verificacao[0])
            if valor == id_usuario:
                verific = 1
        if verific == 0:
            print("Id de usuário não cadastrado, tente novamente")
            sys.exit()

        # Após isso, a variável 'id_livros' irá receber os livros que o usuário
        # deseja pegar emprestado, e logo em seguida a variável 'livros' recebe 
        # uma a variável 'id_livros' com '.split()', transformando uma string
        # em vários 'índices'.
        id_livros = input("Digite o id dos livros exermplo: (11/22/33/44):")
        livros = id_livros.split("/")
        data_validade = input("Digite a data de validade do emprestimo(dd/mm/aa)")
        verific1 = 0

        # Aqui foi colocado um 'for', para pegar do banco de dados o 'id', 'isbn' e a 
        # 'situacao' do livro.
        for linha in cursor.execute("select id, isbn, situacao from livros_cadastrados"):
            # Esse 'for' irá verificar com o banco de dados, para ver ao certo qual
            # livro que o usuário quer pegar.
            for i in livros:
                if str(linha[0]) == i:
                    for j in self.lista_livros:
                        # Esse 'if' procura pelo isbn do livro para ver a situacao do livro,
                        # Se está sendo emprestado ou não.
                        if j.isbn == linha[1]:
                            if linha[2] == "emprestado":
                                # Caso o livro esteja sendo emprestado, ele irá fazer com que
                                # a variável 'verific1' receba 1, e não entre no 'if' da linha
                                # 358.
                                print("Livro já está sendo emprestado.")
                                verific1 = 1
        if verific1 == 0:
            for verificacao in livros:
                verific = 0
                for verificacao_id in cursor.execute("select \
                    id from livros_cadastrados"):
                    valor = str(verificacao_id[0])
                    if verificacao == valor:
                        verific = 1
                        # Ele irá procurar o livro, e daí irpa alterar no banco de dados
                        # a situacao para 'emprestado'.
                        lista = []
                        lista.append("emprestado")
                        lista.append(valor)
                        cursor.execute("update livros_cadastrados set situacao = ? \
                                                            where id = ?", lista)
            if verific == 0:
                print(f"Valor {verificacao} não existe.")
            else:
                # E por fim, é adicionado ao banco de dados o empréstimo.
                self.lista_emprestimos.append(Emprestimo(id_usuario, 
                                    id_livros, data_validade, False))

    def alterar_emprestimo(self):
        """Altera um empréstimo.

        Como os empréstimos possuem validade, a função alterar empréstimo funciona
        como quando uma pessoa vai 'renovar' um livro na biblioteca.
        Ele pede apenas o 'id' do empréstimo para poder descobrir qual 
        empréstimo que o usuário deseja modificar, para então, pedir
        a nova data.
        """
        id_emprestimo = input("Digite o id do emprestimo a ser alterado: ")
        verific = 0
        # Aqui ele procura o id do empréstimo que o usuário deseja alterar.
        for verificacao in cursor.execute("select id from emprestimos_ativos"):
            valor = str(verificacao[0])
            if id_emprestimo == valor:
                verific = 1
        # Caso o empréstimo não exista, a variável 'verific' irá receber manter no 0.
        # e se for 0, irá entrar no 'if' e não no 'else'.
        if verific == 0:
            print("Esse id de emprestimo não está cadastrado")
        # Caso a variável 'verific' seja 1, o 'else' será executado, que permitirá a alteração
        # do empréstimo selecionado.
        else:
            nova_validade = input("Digite a nova data de validade do emprestimo(dd/mm/aa): ")
            lista = []
            lista.append(nova_validade)
            lista.append(id_emprestimo)
            cursor.execute("update emprestimos_ativos set data_validade = ? where id = ?", lista)

    def recuperar_emprestimos(self):
        """Recupera os empréstimos.

        Quando o programa é fechado, as listas perdem aquilo que guardam, então 
        esse método cria todos os objetos para serem apenas adicionados à lista.
        """
        for linha in cursor.execute("select id, id_usuario, id_livros, \
        data_validade from emprestimos_ativos"):
            self.lista_emprestimos.append(Emprestimo(linha[1], linha[2], linha[3], True))

    def remover_emprestimo(self):
        """Remove empréstimos

        Esse método foi criado para pode remover os empréstimos do programa.
        para remover um empréstimo, ele precisa apenas do id do empréstimo.
        """
        id_emprestimo = []
        id_emprestimo.append(int(input("Digite o id do emprestimo que irá deletar: ")))
        # Nessa região ele irá alterar os livros que estão no empréstimo para 
        # 'nao emprestado', simbolizando que dá para pegar um livro novamente.
        for i in cursor.execute("select id_livros from emprestimos_ativos where id = ?", id_emprestimo):
            tmp = str(i[0])
            lista = tmp.split("/")
        for i in lista:
            valores = []
            valores.append("Nao emprestado")
            valores.append(i)
            cursor.execute("update livros_cadastrados set situacao = ? where id = ?", valores)
            
        cursor.execute("delete from emprestimos_ativos where id = ?", id_emprestimo)

# Aqui foi criado o objeto 'biblioteca' utilizando a classe Biblioteca.
biblioteca = Biblioteca()

# Esse "while" fica 'rodando' até que o usuário digite uma certa opção para parar.
while True:
    print("O que desejas fazer?")
    print("")
    print("1 - Adicionar algum usuario.")
    print("2 - Remover algum usuario.")
    print("3 - Listar todos os usuario.")
    print("4 - Adicionar algum livro.")
    print("5 - Remover algum livro.")
    print("6 - Listar todos os livros.")
    print("7 - Fazer algum empréstimo.")
    print("8 - Listar todos os empréstimos.")
    print("9 - Alterar empréstimo.")
    print("10 - Remover empréstimo.")
    print("11 - Sair.")
    print("")

    # Aqui é salvo todas as modificações no banco de dados.
    conexao.commit()

    opcao = int(input("Digite a opção: "))

    # Esses 'if' e 'elif' servem para separar o que o usuário irá fazer.
    if opcao == 1:
        biblioteca.adicionar_usuario()

    elif opcao == 2:
        biblioteca.remover_usuario()
        
    elif opcao == 3:
        for linha in cursor.execute("select * from usuarios_cadastrados"):
            print(linha)

    elif opcao == 4:
        biblioteca.adicionar_livro()

    elif opcao == 5:
        biblioteca.remover_livro()

    elif opcao == 6:
        for linha in cursor.execute("select * from livros_cadastrados"):
            print(linha)

    elif opcao == 7:
        biblioteca.adicionar_emprestimo()

    elif opcao == 8:
        for linha in cursor.execute("select * from emprestimos_ativos"):
            print(linha)

    elif opcao == 9:
        biblioteca.alterar_emprestimo()

    elif opcao == 10:
        biblioteca.remover_emprestimo()

    elif opcao == 11:
        break

# Aqui é fechado a conexão com o arquivo do banco de dados.
conexao.close()