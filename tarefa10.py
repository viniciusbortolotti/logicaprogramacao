def exercicio1():
#início
    numero = int(input('Por favor, insira o seu número: '))
    i = 0
    while i <= numero:
        if i % 5 == 0 and i % 2 != 0: 
            print(i)
        i += 1
#fim
exercicio1()

def exercicio2():
#início
    numero_de_entradas = int(input("Quantos elementos deverá ter a sua lista?: "))
    lista = []
    i = 0
    for i in range (numero_de_entradas):
        lista.append(input("Qual número você deseja adcionar à lista?: "))
    print(lista)
    return(lista)
#fim
exercicio2()

def exercicio3():
#início
  lista = input("Valores: ")
  lista_de_valores = lista.split()
  lista_de_numeros_superiores_que_5 = []
  def funcao_superiores():
    i = 0
    while i < len(lista_de_valores):
      if int(lista_de_valores[i]) > 5:
        lista_de_numeros_superiores_que_5.append(lista_de_valores[i])
        i += 1
      else:
        i += 1
    return lista_de_numeros_superiores_que_5
  funcao_superiores()
  print(lista_de_numeros_superiores_que_5)
#fim
exercicio3()

def exercicio4():
#início
    menu = {
        'a': "PSG",
        'b': "BAYERN"
    }
    opcao = input("Pra quem você torce?: ")
    if opcao in menu:
        print(menu[opcao])
    elif opcao == 'd':
        print("Terminando o programa.")
        quit()
    else:
        print("Inválido")
#fim
exercicio4()
