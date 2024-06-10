import os

class Restaurante:

    def exibir_nome_do_programa():
        print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')

    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        
        Restaurante.restaurantes.append(self)

    def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar restaurantes')
        print('3. Alterar estado do restaurante')
        print('4. Sair\n')
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def voltar_menu_principal():
         input('Digite uma tecla para voltar ao menu principal')

    def opcao_invalida():
        print('Opção inválida\n')
    voltar_menu_principal()
    
    def cadastrar_novo_restaurante():
        exibir_subtitulo('Cadastro de novos restaurantes\n')
        nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
        categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
        dados_do_restaurante ={'nome':nome_restaurante,'categoria':categoria,'ativo':False}
        restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()
    
    @classmethod
    def listar_restaurantes(self):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in self.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')

    def alterar_estado_do_restaurante():
        exibir_subtitulo('Alterando estado do restaurante\n')
        nome=input('Digite o nome do restaurante que deseja alterar o estado: ')
        restaurante_encontrado = False
        
        for restaurante in restaurantes:
            if nome==restaurante['nome']:
                restaurante_encontrado=True
                restaurante['ativo']=not restaurante['ativo']
                mensagem=f'O restaurante {nome} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso!'
                print(mensagem)
                
        if not restaurante_encontrado:
            print(f'O restaurante {nome} não foi encontrado.')
            
    voltar_menu_principal()
    
    def finalizar_app():
        exibir_subtitulo('Finalizar app')


    def exibir_subtitulo(texto):
        os.system('self')
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
            
  

restaurante1=Restaurante('Pão com Banha','Gourmet')
restaurante2=Restaurante('Saco do Feijão','Feijoada')
restaurante3=Restaurante('Bife Sujo','Churrascaria')

Restaurante.exibir_nome_do_programa()
Restaurante.exibir_opcoes()
Restaurante.escolher_opcao()
Restaurante.exibir_subtitulo()
Restaurante.voltar_menu_principal()
Restaurante.cadastrar_novo_restaurante()
Restaurante.listar_restaurantes()
Restaurante.opcao_invalida()
