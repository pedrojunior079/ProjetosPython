print('******************************')
print('*   Jogo da adivinhação 3     *')
print('*   Usando comando if e elif  *')
print('******************************')

numero_secreto = 42
chute_str = int(input('Digite o seu numero: '))
print('Voce digitou: ', chute_str)
chute = int(chute_str)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print('Voce acertou!')
elif(maior):
    print('Voce errou! O seu chute foi maior que o número secreto')
elif(menor):
    print('Voce errou! O seu chute foi menor que o numero secreto')

print('Fim de Jogo!')








