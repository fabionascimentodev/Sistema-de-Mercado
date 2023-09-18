import sys

# Variável para determinar em qual menu o usuário estará
comando = 0

# Mensagem inicial de boas-vindas
print('Bem-vindo ao Hortifruti Nascimento!\n')

# Função para exibir o menu inicial
def mostrar_menu():
    print('1. Iniciar uma nova compra')
    print('2. Adicionar produto ao catálogo')
    print('3. Remover produto do catálogo')
    print('4. Sair do programa')

    # Pega o input do usuário com o valor desejado
    comando = int(input('\nSelecione uma opção digitando um número: '))

    # Envia o valor para a função valida_input
    valida_input(comando)

# Função para terminar a aplicação
def sair():
    print('\nDeseja sair da aplicação?')
    comando = int(input("Digite '0' para sair ou '1' para cancelar e voltar ao menu: "))
    if comando == 0:
        sys.exit()  # Termina a aplicação
    else:
        mostrar_menu()

# Função que verifica qual o input dado pelo usuário e exibe o menu correspondente
def valida_input(valor):
    if valor == 0:
        mostrar_menu()
    elif valor == 1:
        import compra
        compra.compra()
    elif valor == 2:
        import catalogo
        catalogo.adicionar_produto()
    elif valor == 3:
        import catalogo
        catalogo.remover_produto()
    elif valor == 4:
        sair()

# Exibe inicialmente o menu
mostrar_menu()
