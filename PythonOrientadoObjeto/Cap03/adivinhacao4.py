print('******************************')
print('*   Jogo da adivinhação 4     *')
print('*   Usando comando while      *')
print('******************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while(rodada <= total_de_tentativas):
    print('Tentativa{} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite o seu numero: '))
    print('Voce digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
       print('Voce acertou!')
       break
    elif(maior):
       print('Voce errou! O seu chute foi maior que o número secreto')
    elif(menor):
       print('Voce errou! O seu chute foi menor que o numero secreto')

    rodade = rodada + 1

print('Fim de jogo')








