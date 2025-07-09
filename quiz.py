def main():
    pontos = 0

    if mostrar_menu():
        for pergunta in carregar_perguntas():
            if validar_resposta(perguntar_questao(carregar_perguntas()[pergunta]),carregar_perguntas()[pergunta]['resposta']):
                pontos = calcular_pontuacao(pontos)
        mostrar_resultado(pontos,len(carregar_perguntas()))

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
        },
        3:{
            'pergunta':"Qual é o elemento químico representado pelo símbolo 'O'?",
            'alternativas': ['A - Ouro','B - Oxigênio','C - Óxido'],
            'resposta':"b"
        },
        4:{
            'pergunta':"Quem foi o primeiro presidente do Brasil?",
            'alternativas': ['A - Getúlio Vargas','B - Lula','C - Deodoro da Fonseca'],
            'resposta':"c"
        },
        5:{
            'pergunta':"Em que país se localiza a Torre Eiffel?",
            'alternativas': ['A - Itália','B - França','C - Espanha'],
            'resposta':"b"
        }
    }
    return perguntas

def perguntar_questao(questao):
        print(questao['pergunta'])
        print(f"{questao['alternativas'][0]}\n{questao['alternativas'][1]}\n{questao['alternativas'][2]}")
        while True:
            resposta_usuario = input("Qual opção é a correta? ").strip().lower()
            if resposta_usuario == 'a' or resposta_usuario == 'b' or resposta_usuario == 'c':
                return resposta_usuario
            else:
                print("Opção inválida.")

def validar_resposta(resposta, resposta_certa):
    return resposta == resposta_certa

def calcular_pontuacao(pontos):
    pontos += 1
    return pontos

def mostrar_resultado(pontuacao,total):
    print(f"Você acertou: {pontuacao} de {total} perguntas")

main()