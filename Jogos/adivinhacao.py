print('******************************')
print('*   Jogo da adivinhação 5    *')
print('*   Usando comando for       *')
print('******************************')

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas):
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

print('Fim de jogo')