def exercicio1():
#início
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    nota3=float(input("Digite a terceira nota: "))
    soma = nota1+nota2+nota3
    media = soma/3
    return(f"Média do aluno é {media}")
exercicio1()

def exercicio2():
#início
    num_entrada=int(input("Quantos elementos terá a sua lista?: "))
    lista_de_saida = []
    i = 0
    for i in range(num_entrada):
        lista_de_saida.append(input("Quais números você quer adicionar nessa lista?: "))
    return(lista_de_saida)
#fim
exercicio2()

def exercicio3():
#início
    menu = {
        'a': "Globo",
        'b': "SBT"
    }
    opcao = input("Qual canal deseja assistir?: ")
    if opcao in menu:
        print(menu[opcao])
    elif opcao == 'z' or 'Z':
        print("Finalizando o programa.")
        quit()
    else:
        print("Inválido")
#fim
exercicio3()

def exercicio4():
#início
    lista_de_media = [9, 10, 5, 8]
    medias_inferiores_a_sete = []
    i=0
    for i in lista_de_media:
        if i < 7:
            medias_inferiores_a_sete.append([i])
            i += 1
        else:
            i += 1
    porcentagem_etapa1 = len(lista_de_media)-len(medias_inferiores_a_sete)
    porcentagem_etapa2 = porcentagem_etapa1 * 100 
    porcentagem_etapa3 = porcentagem_etapa2/len(lista_de_media)
    porcentagem_final = float(porcentagem_etapa3/100)
    if porcentagem_final < 0.25:
        print("Professor Coxa")
    else:
        print("Professor Padrão")
#fim
exercicio4()
