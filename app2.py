import os

class Restaurante:
    restaurantes=[]

    def __init__(self,nome_restaurante,categoria):
        self.nome_restaurante=nome_restaurante
        self.categoria=categoria
        self.ativo=False
        
        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        return f'{self.nome_restaurante} | {self.categoria}'
    
    
    def exibir_nome_do_programa():
        print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')
    
    
    def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar restaurantes')
        print('3. Alterar estado do restaurante')
        print('4. Sair\n')
        
    
    def voltar_menu_principal():
        input('Digite uma tecla para voltar ao menu principal')
        Restaurante.main()
    

    def opcao_invalida():
        print('Opção inválida\n')
        Restaurante.voltar_menu_principal()
    
    
    def cadastrar_novo_restaurante():
        Restaurante.exibir_subtitulo('Cadastro de novos restaurantes\n')
        nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
        categoria =input(f'Digite a categoria do restaurante {nome_restaurante}: ')
        dados_do_restaurante =Restaurante(nome_restaurante,categoria)
        Restaurante.restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
        Restaurante.voltar_menu_principal()
    
    
    # @classmethod
    # def listar_restaurantes(cls):
    #     print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    #     for restaurante in cls.restaurantes:
    #         print(f'{restaurante.nome_restaurante.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')
    #         Restaurante.voltar_menu_principal()
     
     
    @classmethod       
    def listar_restaurantes(cls):
        Restaurante.exibir_subtitulo('Listando restaurantes')
    
        for restaurante in cls.restaurantes:
            nome_restaurante=restaurante.nome_restaurante
            categoria=restaurante.categoria
            ativo= 'Ativado' if restaurante.ativo else 'Desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
            
        Restaurante.voltar_menu_principal()


    @classmethod
    def alterar_estado_do_restaurante(cls):
        Restaurante.exibir_subtitulo('Alterando estado do restaurante\n')
        nome_do_restaurante=input('Digite o nome do restaurante que deseja alterar o estado: ')
        restaurante_encontrado = False
        
        for restaurante in cls.restaurantes:
            if nome_do_restaurante==restaurante.nome_restaurante:
                restaurante_encontrado=True
                restaurante.ativo=not restaurante.ativo
                if (restaurante.ativo==False):
                    print(f'O restaurante {nome_do_restaurante} foi ativado com sucesso!')
                else: 
                    print(f'O restaurante {nome_do_restaurante} foi desativado com sucesso!')
                    print('')
            
                
        if not restaurante_encontrado:
            print(f'O restaurante {nome_do_restaurante} não foi encontrado.')
            Restaurante.voltar_menu_principal()
    
    
    def finalizar_app():
        Restaurante.exibir_subtitulo('Finalizar app')


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
                Restaurante.cadastrar_novo_restaurante()
            elif opcao_escolhida==2:
                Restaurante.listar_restaurantes()
            elif opcao_escolhida==3:
                print('Ativar Restaurante')
                Restaurante.alterar_estado_do_restaurante()
            else:
                Restaurante.finalizar_app()
        except:
            Restaurante.opcao_invalida()


    def main():
        os.system('cls')
        Restaurante.exibir_nome_do_programa()
        Restaurante.exibir_opcoes()
        Restaurante.escolher_opcao()
        
        if __name__ == '__main__':
            Restaurante.main()

restaurante1=Restaurante('Pão com Banha','Gourmet')
restaurante2=Restaurante('Saco do Feijão','Feijoada')
restaurante3=Restaurante('Bife Sujo','Churrascaria')

Restaurante.exibir_nome_do_programa()
Restaurante.exibir_opcoes()
Restaurante.escolher_opcao()