
def jogar_forca ():
    print("********************************")
    print("Bem vindo ao jogo da foca")
    print("********************************")

    palavra_secreta = "banana"
    acertou = False
    enforcou = False

    while (not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.uper() == letra.uper()):
                print("Ëncontrei a letra {} na posicao {}".format(letra,index))
            index = index + 1
        print("jogando...")

    print("fim do jogo")

if (__name__ == "__main__"):
    jogar_forca()

