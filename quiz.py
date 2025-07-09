def main():
    pontos = 0

    if mostrar_menu():
        for pergunta in carregar_perguntas():
            perguntar_questao(carregar_perguntas()[pergunta])

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
    perguntas = {
        1:{
            'pergunta':"Qual é o maior planeta do sistema solar?",
            'alternativas': ['A - Marte','B - Saturno','C - Júpiter'],
            'resposta':"c",
        },
        2:{
            'pergunta':"Quem escreveu a peça 'Romeu e Julieta'?",
            'alternativas': ['A - Charles Dickens','B - William Shakespeare','C - Machado de Assis'],
            'resposta':"b"
        }
    }
    return perguntas

def perguntar_questao(questao):
        print(questao['pergunta'])
        print(f"{questao['alternativas'][0]}\n{questao['alternativas'][1]}\n{questao['alternativas'][2]}")
        while True:
            resposta = input("Qual opção é a correta? ").strip().lower()
            if resposta == 'a' or resposta == 'b' or resposta == 'c':
                return resposta
            else:
                print("Opção inválida.")

def validar_resposta(resposta, resposta_certa):
    return resposta == resposta_certa

main()