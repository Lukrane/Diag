num = int(input('Escolha um número'))
colunas = num
linhas = num
matriz = [0] * linhas
for cont in range(linhas):
    matriz[cont] = colunas * [0]
    for cont2 in range(colunas):
        matriz[cont][cont2] = int(input(''))
for cont in range(linhas):
    print(matriz[cont])
def diag(matrz):
    absolute1 = 0
    absolute2 = 0
    for cont in range(num):
        absolute1 += matrz[cont][cont]
        absolute2 += matrz[cont][(num - (cont + 1))]
    absolute = absolute1 - absolute2
    if absolute < 0:
        absolute *= -1
    return absolute
print(diag(matriz))