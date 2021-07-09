
def jogar_forca ():
    print("********************************")
    print("Bem vindo ao jogo da foca")
    print("********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Voce ganhou.Parabens!!!")
    else:
        print("Voce perdeu")

    print("fim do jogo")

if (__name__ == "__main__"):
    jogar_forca()

