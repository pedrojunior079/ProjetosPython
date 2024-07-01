def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da forca!***')
    print('*********************************')

    palavra_secreta = 'banana'
    letras_acertas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertas)

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertas
        print(letras_acertas)
        if(acertou):
            print("Voce ganhou!!")
        else:
            print("Voce perdeu!!")
        print("fim de jogo");
