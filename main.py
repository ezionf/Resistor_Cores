numeros = {'preto':'0', 'marrom':'1', 'vermelho':'2', 'laranja':'3', 'amarelo':'4', 'verde':'5', 'azul':'6', 'violeta':'7', 'cinza':'8','branco':'9'}
multiplicador = {'preto':1, 'marrom':10, 'vermelho':100, 'laranja':1000, 'amarelo':10000, 'verde':100000, 'azul':1000000, 'violeta':10000000, 'dourado':0.1, 'prateado':0.01}
tolerancia = {'marrom':1, 'vermelho':2, 'verde':0.5, 'azul':0.25, 'violeta':0.1, 'cinza':0.05, 'dourado':5, 'prateado':10}
numeros['roxo'] = numeros['violeta']
multiplicador['roxo'] = multiplicador['violeta']
multiplicador['ouro'] = multiplicador['dourado']
multiplicador['prata'] = multiplicador['prateado']
tolerancia['roxo'] = tolerancia['violeta']
tolerancia['ouro'] = tolerancia['dourado']
tolerancia['prata'] = tolerancia['prateado']
while True:
    faixa1, faixa2, faixa3, faixa4 = [i for i in input('Insira as cores das quatro faixas apenas espaçadas: ').strip().lower().split()]
    resistencia = int(numeros[faixa1]+numeros[faixa2]) * multiplicador[faixa3]
    if resistencia >= (10**6):
        resistencia = str(int(resistencia/(10**6)))+' M'
    elif resistencia >= (10**3):
        resistencia = str(int(resistencia/(10**3)))+' K'
    else:
        resistencia = str(int(resistencia))+' '
    print(f'O seu resistor com as cores {faixa1}, {faixa2}, {faixa3} e {faixa4} tem uma resistência de {resistencia}Ω com uma tolerância de {tolerancia[faixa4]}%.')
    escolha = input('Deseja utilizar o programa novamente?\nS para sim\nN para não\n').upper().strip()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Deseja utilizar o programa novamente?\nS para sim\nN para não\n').upper().strip()
    if escolha == 'N':
        break
print('Obrigado por usar o programa :D')
quit()