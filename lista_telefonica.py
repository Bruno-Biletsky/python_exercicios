"""RMs
Enrico Ricarte - RM558571
Victor Freire - RM556191
Bruno Biletsky - RM554739
"""
contatos = {
 'Mariana': {'telefones': ['(11)98456-1234', '(11)97543-8875', '(21)98548-1345'], 'email': 'mariana@email.com'},
 'João': {'telefones': ['(11)94975-3333'], 'email': 'joao@email.com'},
 'Rodrigo': {'telefones': ['(21)98234-2215', '(21)99458-6791'], 'email': 'rodrigo@email.com'},
 'Aninha': {'telefones': ['(11)98874-2314', '(11)97765-4321'], 'email': 'aninha@email.com'},
 'Luciana': {'telefones': ['(21)98765-4321', '(21)99888-7766', '(21)91234-5678'], 'email': 'luciana@email.com'},
 'Pedro': {'telefones': ['(31)93333-8888'], 'email': 'pedro@email.com'},
 'Amanda': {'telefones': ['(31)95555-7777', '(31)96666-4444'], 'email': 'amanda@email.com'},
 'Fernando': {'telefones': ['(51)92222-1111', '(51)93333-2222', '(51)94444-3333'], 'email': 'fernando@email.com'},
 'Sofia': {'telefones': ['(51)94444-3333'], 'email': 'sofia@email.com'}
}
def opcao()->str:
    """A função mostra as opções para o user e retorna a opção escolhida"""
    print("""
    1 - Adicionar novos contatos. 
    2 - Remover contatos existentes.
    3 - Consultar telefones e e-mail de um contato.
    4 - Inserir um novo telefone a um contato.
    5 - Alterar o e-mail de um contato.
    6 - Sair.
    """)
    op:str = input("Selecione a opção: ")
    return op

def mostar_contato():
    print(contatos)

def consultar_contato(nome: str) -> None:
    """A função permite consultar os telefones e email do contato selecionado"""
    if nome in contatos:
        print(f"email do(a) {nome}: ", contatos[nome]["email"])
        for telefone in contatos[nome]["telefones"]:
            print(f"Telefone: {telefone}")

def adicionar_contato()->None:
    """A função pede o nome do contato e adiciona a ele:\n
    - Telefones
    - Email
    """
    nome:str = input("Digite o nome do contato: ")
    if nome not in contatos:
        contatos[nome] = {
            'telefones': [],
            'email': input(f"digite o email do {nome}: ")
        }
        while True:
            telefone:str = input(f"Digite o telefone do {nome}: ")
            if telefone == '':
                break
            else:
                print('inserido com sucesso')
                contatos[nome]["telefones"].append(telefone)
        consultar_contato(nome)
def remover_contato()->None:
    """Função que remove o contato INTEIRO seleciondo"""
    nome:str = input('digite o nome do contato: ')
    if nome in contatos:
        contatos.pop(nome)
        print('contato removido!')
    else:
        print('Contato não está na lista')
    for nome in contatos.keys():
        print("-----------------------------------------------------------------")
        consultar_contato(nome)
def adicionar_info()->None:
    """A função permite adicionar um telefone ao contato selecionado (pré-existente)"""
    nome:str = input("Digite o nome do contato: ")
    if nome in contatos:
        telefone:str = input("Digite o numero a ser adicionado: ")
        contatos[nome]["telefones"].append(telefone)
        print(f"{nome}: ", contatos[nome])
    else:
        print('Contato não existe')
    consultar_contato(nome)
def alterar_email()->None:
    """A função permite alterar o email do contato selecionado (pré-existente)"""
    nome:str = input("Digite o nome do contato: ")
    if nome in contatos:
        email_novo:str = input("Digite o novo email a ser adicionado: ")
        contatos[nome]["email"] = email_novo
        print(f"{nome}: ", contatos[nome]["email"])
    else:
        print('Contato não existe')
    consultar_contato(nome)
def menu()->bool:
    """ Função que executa o caso selecionado previamente"""
    match opcao():
        case '1':
            # adicionar novo contato
            adicionar_contato()
        case '2':
            # remover contatos existentes
            remover_contato()
        case '3':
            # Consultar telefone e email de um contato
            consultar:str = input('Digite o nome a ser consultado: ')
            consultar_contato(consultar)
        case '4':
            # Inserir um novo telefone a um contato
            adicionar_info()
        case '5':
            # Alterar o email de um contato
            alterar_email()
        case '6':
            print('Finalizando programa...')
            return True
        case _:
            print('opção inválida!')
while True:
    if menu()==True:
        break
