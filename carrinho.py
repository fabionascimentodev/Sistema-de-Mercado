# Lista para exibir quais produtos estão no carrinho do cliente
carrinho_produtos = []

# Função para exibir o carrinho de compras do cliente atual
def mostrar_carrinho():
    import compra

    print('Você adicionou os seguintes itens ao carrinho:')
    
    if not carrinho_produtos:
        print('O carrinho está vazio.')
    else:
        for item in carrinho_produtos:
            print(item)

    print("\nPara finalizar o carrinho digite '0'")
    print("Para adicionar mais itens ao carrinho digite '1'")
    print("Para remover itens do carrinho digite '2'")
    opcao = int(input('\nOpção desejada: '))

    if opcao == 0:
        finalizar_carrinho()
    elif opcao == 1:
        compra.compra()
    elif opcao == 2:
        remover_produto_carrinho()
    else:
        print('Comando inválido! Retornando...')
        mostrar_carrinho()

# Função para remover um produto do carrinho de compras do cliente atual
def remover_produto_carrinho():
    deseja_continuar = 's'

    while deseja_continuar == 's':
        print('\nVocê adicionou os seguintes itens: ', carrinho_produtos)
        produto = input('\nDigite o nome do produto que deseja remover: ').lower()

        if produto in carrinho_produtos:
            print(f'{produto} removido com sucesso!')
            carrinho_produtos.remove(produto)

            deseja_continuar = input("Deseja remover mais algum item? Digite 'S' para confirmar e 'N' para fechar o carrinho: ").lower()

            if deseja_continuar not in ('s', 'n'):
                print('\nComando inválido! Retornando...')
                deseja_continuar = 's'

            if deseja_continuar == 'n':
                break
        else:
            print(f'{produto} não encontrado! Retornando...\n')

    finalizar_carrinho()

# Função para finalizar a compra e reexibir o menu
def finalizar_carrinho():
    if not carrinho_produtos:
        print('\nO carrinho está vazio.')
    else:
        print('\nVocê comprou os seguintes itens:')
        for item in carrinho_produtos:
            print(item)
        
        print('Obrigado! Retornando ao menu...')
        zerar_carrinho()
    voltar_ao_menu()

# Função para limpar os itens em carrinho_produtos
def zerar_carrinho():
    carrinho_produtos.clear()

def voltar_ao_menu():
    import main
    main.mostrar_menu()
