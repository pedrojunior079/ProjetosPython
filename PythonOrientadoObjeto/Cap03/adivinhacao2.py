print('******************************')
print('*   Jogo da adivinhação 2     *')
print('******************************')

numero_secreto = 42
chute = int(input('Digite o seu numero: '))
print('Voce digitou: ', chute)

if(numero_secreto == chute):
    print('Voce acertou!')
elif(chute > numero_secreto):
    print('Voce errou! O seu chute foi maior que o número secreto')
elif(chute < numero_secreto):
    print('Voce errou! O seu chute foi menor que o numero secreto')








