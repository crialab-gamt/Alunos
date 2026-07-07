import random
pontos = 0
jogando = True

print ("JOGO DE DADOS")

while jogando:
    dados = random.randint(1,6)
    print ("você tirou o número ", dados)
    if dados == 6:
        pontos += 6 
    elif dados == 4:
        pontos += 4
    elif dados == 2:
        pontos -= 1
    else: 
        pontos += 1
    print ("pontuação final ", pontos)
    escolha = input ("continuar? s/n")
    if escolha.lower () == "n":
        jogando = False
    print ("pontuação final ", pontos)