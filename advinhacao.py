def jogar_advinhacao():
    import random

    print("********************************")
    print("Bem vindo ao jogo de advinhacao")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    nivel = int(input("Fácil(1), Médio(2) Difícil(3)"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("********************************")
        print("rodada {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero de 1 a 100: ")
        chute = int(chute_str)
        print("Voce digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("voce acertou e fez {} pontos!" .format(pontos))
            break
        else:
            if (maior):
                print("voce chutou maior que o numero")
            elif (menor):
                print("voce chutou menor que o numero")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("fim do jogo")

if (__name__ == "__main__"):
    jogar_advinhacao()

