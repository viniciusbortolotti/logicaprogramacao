def calcula_soma( lista ):
    numeros = input()
    soma_dos_numeros = sum(numeros)
    return soma_dos_numeros

def converte_entrada( texto ):
    numeros = '3 8 9 2 0'
    entrada = input(numeros)
    texto = str(entrada)
    lista_dos_numeros = texto.split()
    print(lista_dos_numeros)

def processa_numeros( lista ):
    lista_de_numeros = []
    lista_de_numeros = input()
    val1 = sum(lista_de_numeros)
    val2: int = len(lista_de_numeros)
    return val1, val2

def main():
    entrada = input()
    lista = entrada.split()
    media = sum(lista)/len(lista)
    return media

retorno = main()
print(retorno)
