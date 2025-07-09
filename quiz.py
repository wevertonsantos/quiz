def main():
    perguntas = ["Qual é o maior planeta do sistema solar?","Quem escreveu a peça 'Romeu e Julieta'?"] 

    mostrar_menu()

def mostrar_menu():
    while True:
        try:
            escolha = int(input("Escolha uma opção:\n1. Jogar\n2. Sair\nOpção: "))
            if escolha == 1:
                ...
            elif escolha == 2:
                print("Obrigado. Até logo!")
                break
            else:
                print("Não existe essa opção, escolha outra.")
        except ValueError:
            print("Você digitou algo errado. Tente novamente!")

main()