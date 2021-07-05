import advinhacao
import forca

print("********************************")
print("******* Escolha o jogo *********")
print("********************************")

jogo = int(input("Advinhacao [1] , Foca [2]: "))

if (jogo == 1):
    advinhacao.jogar_advinhacao()
elif (jogo == 2):
    forca.jogar_forca()

print("fim do jogo")

