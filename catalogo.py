# Lista para exibir os produtos disponíveis
catalogo_produtos = ['maçã', 'banana', 'uva', 'mamão', 'pêssego']

# Função para adicionar um produto ao catálogo de produtos
def adicionar_produto():
    print('\nVocê está adicionando um novo produto.')

    novo_produto = input('\nDigite um nome para o produto a ser adicionado: ').lower()

    # Verifica se o produto especificado já existe
    if novo_produto in catalogo_produtos:
        print(f'\n{novo_produto} já existe no catálogo! Retornando ao menu...\n')
    else:
        catalogo_produtos.append(novo_produto)
        print(f'{novo_produto} adicionado(a) com sucesso ao catálogo! Retornando ao menu...\n')

# Função para remover um produto do catálogo de produtos
def remover_produto():
    deseja_continuar = 's'

    print('\nVocê está removendo um produto existente.')

    while deseja_continuar == 's':
        print('Produtos no catálogo: ', catalogo_produtos)

        # Verifica se a lista está vazia
        if not catalogo_produtos:
            print('\nNão existem itens no catálogo! Retornando ao menu...\n')
        else:
            produto = input('\nDigite o nome do produto a ser removido: ').lower()

            # Verifica se o produto especificado está na lista, caso sim, remova-o
            if produto in catalogo_produtos:
                catalogo_produtos.remove(produto)
                print(f'{produto} removido(a) com sucesso! Retornando ao menu...')
            else:
                deseja_continuar = input(f'{produto} não foi encontrado! Pressione "S" para tentar novamente ou "N" para voltar ao menu: ').lower()

                if deseja_continuar not in ('s', 'n'):
                    print('Comando inválido! Retornando...')
                    deseja_continuar = 's'

                # Se a resposta é 'n', saia do loop
                if deseja_continuar == 'n':
                    break

# Função para retornar ao menu
def voltar_ao_menu():
    import main
    main.mostrar_menu()
