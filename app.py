import os      #importar um biblioteca ja instalada com o python

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo':False}, 
                {'nome': 'Tacos', 'categoria': 'Tacos', 'ativo':True},
                {'nome': 'PizzariaSuprema', 'categoria': 'Pizzaria', 'ativo':False}              
]                       #criar uma lista
                                         
def exibir_nome_do_programa(): 
    '''Exibe o nome do progrma na tela '''
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)
    
def exibir_opcoes():
    '''Mostra as opções disponiveis do programa no menu principal'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Opção responsavel por finalizar o app'''
    os.system('cls')                                    #limpar a linha antes de uma função
    print('Finalizando App\n')

def voltar_ao_menu_principal():
    '''Responsavel por voltar ao menu principal'''
    input('\nDigite uma tecla para voltar para o menu. ')
    main()

def opcao_invalida():
    '''Exibe uma mensagem de erro caso acha algo de errado com o código'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal() 

def exibir_subtitulo(texto):
    '''Gera os subtitulos de cada aba do programa'''
    linha = '*' * (len(texto) + 4)
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)


def cadastrar_novo_restaurante():
    ''''Essa função é responsavel por cadastrar um novo restaurante
    Ipunts:
    -Nome do Restaurante
    -Categoria

    -Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes.\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_dos_restaunrante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False,}
    restaurantes.append(dados_dos_restaunrante)

    print(f'O restaurante {nome_do_restaurante}, ja foi cadastrado em nosso sistema!')    
    voltar_ao_menu_principal()                                           

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes Cadastrados!\n')

    print(f'{'Nome do Restaurante'.ljust(23)}|{'Categoria'.ljust(21)}|{'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} |{categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando Estado do Restaurante.')
    nome_restaurante = input('Digite o nome do Restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativdo com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = input('Escolha uma opção: ')

        opcao_escolhida =int(opcao_escolhida)                   #tranformar uma variavel de um tipo para outro tipo
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
     
def main():            #definir uma função
    os.system('cls')                                 
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()