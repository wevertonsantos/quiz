def main():
    pontos = 0

    if mostrar_menu():
        for pergunta in carregar_perguntas():
            validar_resposta(perguntar_questao(pergunta,carregar_perguntas()),'c')

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
    lista_perguntas = {
        1:{
            'pergunta':"Qual é o maior planeta do sistema solar?",
            'resposta':""
        }
    }
    return ["Qual é o maior planeta do sistema solar?","Quem escreveu a peça 'Romeu e Julieta'?","Em que país se localiza a Torre Eiffel?","Qual é o elemento químico representado pelo símbolo 'O'?","Quem foi o primeiro presidente do Brasil?"]

def perguntar_questao(questao,perguntas):
    if perguntas.index(questao) == 0:
        print(questao)
        resposta = input("A - Marte\nB - Saturno\nC - Júpiter\nOpção: ").strip().lower()
        if resposta == "a" or resposta == "b" or resposta == "c":
            return resposta
        else:
            print("Resposta não existe.")
    elif perguntas.index(questao) == 1:
        print(questao)
        resposta = input("A - Charles Dickens\nB - William Shakespeare\nC - Machado de Assis\nOpção: ").strip().lower()
        if resposta == "a" or resposta == "b" or resposta == "c":
            return resposta
        else:
            print("Resposta não existe.")

def validar_resposta(resposta, resposta_certa):
    return resposta == resposta_certa

main()