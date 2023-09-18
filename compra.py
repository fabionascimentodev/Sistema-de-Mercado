import carrinho
import catalogo
import main  # Importe o módulo 'main' aqui para evitar problemas de ciclo de importação.

# Função para exibir o menu de compra
def compra():
    # Inicia uma variável 'indice' com valor 0, para se ajustar à lista
    indice = 0
    deseja_continuar = 's'

    print('\nCatálogo de Produtos: ')

    for i, produto in enumerate(catalogo.catalogo_produtos):
        # Exibe o índice no loop atual e o item da lista
        print(f'{i} - {produto}')

    while deseja_continuar == 's':
        numero = int(input('\nDigite um número para o item desejado: '))

        if numero < 1 or numero >= len(catalogo.catalogo_produtos):
            print('Número inválido! Retornando...\n')
            voltar_ao_menu()
        else:
            item = catalogo.catalogo_produtos[numero]
            carrinho.carrinho_produtos.append(item)

        deseja_continuar = input("Digite 'S' se deseja selecionar outro item OU digite 'N' se deseja finalizar o carrinho: ").lower()

        if deseja_continuar not in ('s', 'n'):
            print('Comando inválido! Retornando...\n')
            deseja_continuar = 's'

    # Chama 'mostrar_carrinho' caso saia do while
    carrinho.mostrar_carrinho()

# Função para voltar ao menu principal
def voltar_ao_menu():
    main.mostrar_menu()
