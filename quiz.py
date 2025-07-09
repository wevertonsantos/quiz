def main():

    if mostrar_menu():
        for pergunta in carregar_perguntas():
            print(pergunta)

def mostrar_menu():
    while True:
        try:
            escolha = int(input("Escolha uma opção:\n1. Jogar\n2. Sair\nOpção: "))
            if escolha == 1:
                return True
            elif escolha == 2:
                print("Obrigado. Até logo!")
                return False
            else:
                print("Não existe essa opção, escolha outra.")
        except ValueError:
            print("Você digitou algo errado. Tente novamente!")

def carregar_perguntas():
    return ["Qual é o maior planeta do sistema solar?","Quem escreveu a peça 'Romeu e Julieta'?","Em que país se localiza a Torre Eiffel?","Qual é o elemento químico representado pelo símbolo 'O'?","Quem foi o primeiro presidente do Brasil?"]

main()