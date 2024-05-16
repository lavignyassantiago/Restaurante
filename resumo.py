import os
#os = sistema operacional

#restaurantes = ['Lala', 'KFC']
restaurantes = [{'nome': 'Ragazzo', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Pizza Hut', 'categoria': 'Fast food', 'ativo': False},
                {'nome': 'Burguer King', 'categoria': 'Fast food', 'ativo': True},
                {'nome': 'Cantina Toscana', 'categoria': 'Italiana', 'ativo': True}, 
                ]


def exibir_nome_do_programa():
   print(""" 
      
✩ ⋆｡°  🍕🍟🥪 𝓡𝓔𝓢𝓣𝓐𝓤𝓡𝓐𝓝𝓣𝓔 𝓓𝓐 𝓛𝓐𝓛𝓐  🥙🥡🍖  ⋆｡°✩
       """)

def exibir_opcao():
  print("🦋 1. Cadastrar Restaurante")
  print("🦋 2. Listar Restaurantes")
  print("🦋 3. Ativar Restaurante")
  print("🦋 4. Sair")

def finalizar_app():
#def = definir função
    exibir_subtitulo("Finalizando o app")
    #limpar o menu e retornar apenas:

def opcao_invalida():
    print("Opção invalida!\n")
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('Pressione o botão enter para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes 🍟 \n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("Digite a categoria do restaurante que deseja cadastrar: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False} # mostra oque  queremos passar de informação ali de cima
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} com categoria {categoria}, foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo(f"Listando os restaurantes de Osasco 🍟 \n")

    for restaurante in restaurantes: #for = laço de repetição
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f"✿ - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}")
        voltar_ao_menu_principal()    

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()
        
    


def escolher_opcao():
    try:
        opção_escolhida = int(input("Escolha a sua opção: "))
        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()
            print("Ativar Restaurante")
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
       

def main():
    exibir_nome_do_programa()
    exibir_opcao()#exibe tudo novamente
    escolher_opcao()

if __name__ == '__main__':
    main()
