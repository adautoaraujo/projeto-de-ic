import math


def tanque_septico(numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao):
    """Função que calcula o volume do tanque séptico."""
    volume_tanque = (1000 + numero_contribuintes * ((contribuicao_despejos*periodo_retencao) + (tempo_acumulacao*contribuicao_lodo)))
    return volume_tanque


def dimensoes_tanque(volume_m3, altura_tanque):
    """função que calcula as dimensões do tanque séptico"""
    abase_tanque = (volume_m3 / altura_tanque)
    largura_tanque = ((abase_tanque / 2) ** 0.5)
    comprimento_tanque = (largura_tanque * 2)
    print("As dimensões do tanque séptico são:")
    print("Altura = ", "%.2f" % altura_tanque, "m")
    print("Comprimento = ", "%.2f" % comprimento_tanque, "m")
    print("Largura = ", "%.2f" % largura_tanque, "m")


def filtro_anaerobio(numero_contribuintes, contribuicao_despejos, periodo_retencao):
    """função que calcula as dimensões do filtro anaeróbio"""
    volume_filtro = (1.6 * numero_contribuintes * contribuicao_despejos * periodo_retencao)
    flag = True
    while flag:
        try:
            altura_filtro = float(input("Insira a altura desejada para o filtro anaeróbio em m:"))
            if 0 >= altura_filtro:
                print("Insira uma altura maior que 0!")
            else:
                flag = False
        except:
            print("Insira um número maior que 0!")
    print("O volume útil do filtro anaeróbio é de", "%.2f" % volume_filtro, "L ou", "%.2f" % (volume_filtro / 1000), "m³")
    abase_filtro = ((volume_filtro / 1000) / altura_filtro)
    largura_filtro = ((abase_filtro / 2)**0.5)
    comprimento_filtro = (largura_filtro * 2)
    print("A seção horizontal do filtro anaeróbio é de", "%.2f" % abase_filtro, "m²")
    print("As dimensões do filtro anaeróbio são:")
    print("Altura = ", "%.2f" % altura_filtro, "m")
    print("Comprimento = ", "%.2f" % comprimento_filtro, "m")
    print("Largura = ", "%.2f" % largura_filtro, "m")


def sumidouro(coeficiente_infiltracao, numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao):
    """função que calcula a área de infiltração e o diâmetro do sumidouro"""
    area_infiltracao = (tanque_septico(numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao) / coeficiente_infiltracao)
    print("A área de infiltração do sumidouro é de", "%.2f" % area_infiltracao, "m²")
    flag = True
    while flag:
        try:
            altura_sumidouro = float(input("Insira a altura que gostaria de adotar para o sumidouro, em m:"))
            if altura_sumidouro <= 0:
                print("A altura deve ser positiva!")
            else:
                flag = False
        except:
            print("Insira um número!")
    diametro_sumidouro = (area_infiltracao / (math.pi * altura_sumidouro))
    print("O diâmetro do sumidouro é de:", "%.2f" % diametro_sumidouro, "m")


def vala_infiltracao(contribuicao_diaria, coeficiente_infiltracao):
    """calcula o campo de absorção, comprimento da vala e o tamanho dos ramais"""
    area_absorcao = (contribuicao_diaria / coeficiente_infiltracao)
    flag = True
    while flag:
        try:
            largura_vala = float(input("Insira a largura que gostaria de adotar para a vala entre 0.5 m e 1 m:"))
            if (largura_vala >= 0.5) and (largura_vala <= 1):
                flag = False
            else:
                print("A largura deve estar entre 0.5 m e 1 m")
        except:
            print("Insira um número entre 0.5 m e 1 m!")
    print("O campo de absorção da vala de infiltração é de:", "%.2f" % area_absorcao, "m²")
    comprimento_vala = (area_absorcao / largura_vala)
    print("O comprimento da vala é de:", "%.2f" % comprimento_vala, "m")

    flag = True
    while flag:
        try:
            numero_ramais = int(input("Insira o número de ramais:"))
            if(numero_ramais > 0):
                flag = False
            else:
                print("Insira um número maior que 0!")
        except:
            print("Insira um número inteiro!")
    tamanho_ramais = (comprimento_vala / numero_ramais)
    print("O tamanho dos ramais é de", "%.2f" % tamanho_ramais, "m")


def modulo_principal():
    """função que recebe as informações principais"""
    try:
        numero_contribuintes = int(input("Insira o número de habitantes(no mínimo 5 contribuintes):"))
        if numero_contribuintes < 5:
            print("No mínimo 5 contribuintes!")
            modulo_principal()
    except:
        print("É necessário um número inteiro!")
        modulo_principal()

    padrao = input("Insira o padrão da residência('a' para alto, 'm' para médio ou 'b' para baixo):").lower()
    while(padrao != "a" and padrao != "m" and padrao != "b"):
        print("Padrão inválido!")
        padrao = input("Insira o padrão da residência(a para alto, m para médio ou b para baixo):").lower()
    flag = True
    while flag:
        try:
            intervalo_limpeza = int(input("Insira o intervalo de limpeza do tanque séptico em anos (1 a 5):"))
            if intervalo_limpeza <= 5 and intervalo_limpeza >= 1:
                flag = False
            else:
                print("O intervalo de limpeza deve estar entre 1 e 5 anos")
        except:
            print("Insira um número inteiro!")
    flag = True
    while flag:
        try:
            temperatura_ambiente = float(input("Insira a temperatura ambiente do mês mais frio em ºC:"))
            flag = False
        except:
            print("Insira um número!")
    calculos(numero_contribuintes, padrao, intervalo_limpeza, temperatura_ambiente)


def recursividade():
    print("")
    entrada = input("Deseja realizar outro dimensionamento?(S ou N):").lower()
    if(entrada == "s"):
        modulo_principal()
    else:
        print("Obrigado por usar o programa!")


def calculos(numero_contribuintes, padrao, intervalo_limpeza, temperatura_ambiente):
    """função que realiza a analise das informações entradas"""
    # valores de contribuição de despejos e contribuição de lodo, nessa ordem
    dic_padrao = {"a": [160, 1], "m": [130, 1], "b": [100, 1]}
    contribuicao_despejos = dic_padrao[padrao][0]
    contribuicao_lodo = dic_padrao[padrao][1]
    # tempo de acumulação de acordo com a temperatura
    dic_intervalolimpeza = {1: [94, 65, 57], 2: [134, 105, 97], 3: [174, 145, 137], 4: [214, 185, 177], 5: [254, 225, 217]}
    lista_acumulacao = dic_intervalolimpeza[intervalo_limpeza]
    if(temperatura_ambiente < 10):
        tempo_acumulacao = lista_acumulacao[0]
    elif(10 <= temperatura_ambiente <= 20):
        tempo_acumulacao = lista_acumulacao[1]
    elif(temperatura_ambiente > 20):
        tempo_acumulacao = lista_acumulacao[2]

    contribuicao_diaria = (numero_contribuintes * contribuicao_despejos)

    if(contribuicao_diaria < 1500):
        periodo_retencao = 1
    elif(1501 <= contribuicao_diaria <= 3000):
        periodo_retencao = 0.92
    elif(3001 <= contribuicao_diaria <= 4500):
        periodo_retencao = 0.83
    elif(4501 <= contribuicao_diaria <= 6000):
        periodo_retencao = 0.75
    elif(6001 <= contribuicao_diaria <= 7500):
        periodo_retencao = 0.67
    elif(7501 <= contribuicao_diaria <= 9000):
        periodo_retencao = 0.58
    elif(contribuicao_diaria > 9000):
        periodo_retencao = 0.5

    volume_m3 = (tanque_septico(numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao) / 1000)

    if(volume_m3 < 6):
        profundidade_minima, profundidade_maxima = 1.2, 2.2
    elif(6 <= volume_m3 <= 10):
        profundidade_minima, profundidade_maxima = 1.5, 2.5
    elif(volume_m3 > 10):
        profundidade_minima, profundidade_maxima = 1.8, 2.8

    print("O volume útil do tanque séptico prismático é de",\
          "%.2f" % tanque_septico(numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao), "L ou", end=" ")
    print("%.2f" % volume_m3, "m³")
    flag = True
    while flag:
        try:
            altura_tanque = float(input("Insira a altura que gostaria de adotar para o tanque séptico entre \
%.2f m e %.2f m:" % (profundidade_minima, profundidade_maxima)))
            if (altura_tanque >= profundidade_minima)and(altura_tanque <= profundidade_maxima):
                flag = False
            else:
                print("A profundidade deve estar entre %.2f m e %.2f m!" % (profundidade_minima, profundidade_maxima))
        except:
            print("Insira um número!")
    dimensoes_tanque(volume_m3, altura_tanque)
    print("")
    filtro_anaerobio(numero_contribuintes, contribuicao_despejos, periodo_retencao)
    print("")
    flag = True
    while flag:
        try:
            coeficiente_infiltracao = float(input("Insira o coeficiente de infiltração do sumidouro em (L/m²)xdia:"))
            if coeficiente_infiltracao <= 0:
                print("Insira um número maior que 0!")
            else:
                flag = False
        except:
            print("Insira um número!")
    sumidouro(coeficiente_infiltracao, numero_contribuintes, contribuicao_despejos, contribuicao_lodo, periodo_retencao, tempo_acumulacao)
    print("")
    vala_infiltracao(contribuicao_diaria, coeficiente_infiltracao)
    recursividade()


print("Programa de dimensionamento de sistema de tratamento de esgoto residencial")

# main
modulo_principal()
