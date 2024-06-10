# print('Olá, mundo')

import os

#restaurantes=['PythonBurguer','Madalousso','Notubo']
# dicionario
    
restaurantes=[{'nome':'Pão com Banha','categoria':'Gourmet','ativo':False},
              {'nome':'Saco do Feijão','categoria':'Feijoada','ativo':True},
              {'nome':'Bife Sujo','categoria':'Churrascaria','ativo':False}]

def exibir_nome_do_programa():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
    
def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar um novo restaurante
    
        Inputs:
        -Nome do restaurante
        -Categoria
        
        Outputs:
        -Adiciona um novo restaurante ao dicionário restaurantes
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante ={'nome':nome_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        ativo= 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_menu_principal()
    
def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante\n')
    nome_restaurante=input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
        
    voltar_menu_principal()
    
def finalizar_app():
    exibir_subtitulo('Finalizar app')
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opcao():
    try:
        opcao_escolhida=int(input("Escolha uma opção: "))
        
        if opcao_escolhida==1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            listar_restaurantes()
        elif opcao_escolhida==3:
            print('Ativar Restaurante')
            alterar_estado_do_restaurante()
        else:
            finalizar_app()
    except:
        opcao_invalida
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()