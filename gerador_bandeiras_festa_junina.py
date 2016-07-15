cores = ['azuis','amarelas','verdes','vermelhas']
dict_bandeiras = {}


print('*************************************')
print('Festa Junina - ver.1')
print('Módulo Gerador de bandeirinhas')
print('*************************************')
print('')
print ('Numero dos Código das Cores')
for cont in range (len(cores)):
    print('{} - {}'.format(cont,cores[cont]))



def gerador():
    while True:
        cod_cor = input('Insira o Código da cor:')
        if cod_cor.isdigit():
            cod_cor = int(cod_cor)
            if cod_cor >= 0 and cod_cor <= 3:
                cor_selecionada = cores[cod_cor]
                break
            else:
                cod_cor = str(cod_cor)
                print('Erro: O codigo digitado não existe')

        elif cod_cor.isalnum():
            print('Erro: Não é permitido Letras')

        else:
            print('Erro: Só é permitido Números')
            
    qtd = int(input('quantidade: '))
    if cor_selecionada in dict_bandeiras:
        for item in dict_bandeiras:
            if item == cor_selecionada:
                novo_valor = dict_bandeiras[item] + qtd
                dict_bandeiras.update({item:novo_valor})
                
    else:
        dict_bandeiras.__setitem__(cor_selecionada,qtd)
        


while True:
    decisao_gerador = input('Aperte "Enter" para continuar...')
    if decisao_gerador == '':
        gerador()
    else:
        print('Você decidiu interromper!')
        break
print('')
print('*************************************************')
print('**              Pedido Registrado              **')
print('*************************************************')
print('')
for item in dict_bandeiras:
    if dict_bandeiras[item] >= 1:
        print('-> {} bandeiras {}'.format(dict_bandeiras[item],item))
print('')
print('*************************************************')

