'''
    Recebe string de 8 bit's de 0's e 1's convertendo os bit's em decimais
    mostrando na tela a converção dos valores. '''
while True:
    binario = str(input("Conveter BINARIO para DECIMAL: "))
    if "01" == binario:
        print("Apenas 0's e 1's!!!")
        continue
    if len(binario) !=  8:
        print("Só pode conter 8 caracteres!!!")
        continue
    else:
        break


def decimal_converter(binario):
    indice = -1
    resultado = 0

    for i in range(len(binario)):
        multi = int(binario[indice]) * 2**i
        indice -= 1
        resultado += multi
    return resultado

print(f"Binario: {binario} \nDecimal: {decimal_converter(binario)}")