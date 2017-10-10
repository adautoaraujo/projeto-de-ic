import math


def tanque_septico(n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao):
    """Função que calcula o volume do tanque séptico."""
    v_util = (1000+n_contri*((contri_despejos*p_retencao)+(t_acumulacao*contri_lodo)))
    return v_util


def dimensoes_tanque(vol_m3, h_tanque):
    """função que calcula as dimensões do tanque septico"""
    ab_tanque = (vol_m3/h_tanque)
    l_tanque = ((ab_tanque/2)**0.5)
    c_tanque = (l_tanque * 2)
    print("As dimensões do tanque séptico são: altura= %.2f m, \
comprimento= %.2f m e largura= %.2f m" % (h_tanque, c_tanque, l_tanque))


def filtro_anaerobio(n_contri, contri_despejos, p_retencao):
    """função que calcula as dimensões do filtro anaeróbio"""
    v_util = (1.6*n_contri*contri_despejos*p_retencao)
    flag = True
    while flag:
        try:
            h_filtro = float(input("Insira a altura desejada para o filtro anaerobio:"))
            if h_filtro <= 0:
                print("Altura invalida. Insira uma altura valida.")
            else:
                flag = False
        except:
            print("Insira um numero maior que 0!")
    print("O volume útil do filtro anaeróbio é de", "%.2f" % v_util, "L ou", "%.2f" % (v_util/1000), "m³")
    ab_filtro = ((v_util/1000)/h_filtro)
    l_filtro = ((ab_filtro/2)**0.5)
    c_filtro = (l_filtro * 2)
    print("A seção horizontal do filtro anaeróbio é de", "%.2f" % ab_filtro, "m²")
    print("As dimensões do filtro anaeróbio são: altura= %.2f m, \
comprimento= %.2f m e largura= %.2f m" % (h_filtro, c_filtro, l_filtro))


def sumidouro(c_infil, n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao):
    """função que calcula a área de infiltração e o diametro do sumidouro"""
    area_infil = (tanque_septico(n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao)/c_infil)
    print("A área de infiltração do sumidouro é de", "%.2f" % area_infil, "m²")
    h_sumidouro = float(input("Insira a altura que gostaria de adotar para o sumidouro, em m:"))
    while(h_sumidouro <= 0):
        print("A altura deve ser maior que 0")
        h_sumidouro = float(input("Insira a altura que gostaria de adotar para o sumidouro, em m:"))
    diametro_s = (area_infil/(math.pi*h_sumidouro))
    print("O diâmetro do sumidouro é de:", "%.2f" % diametro_s, "m")


def vala_infil(contri_diaria, c_infil):
    """calcula o campo de absorção, comprimento da vala e o tamanho dos ramais"""
    area_abs = (contri_diaria/c_infil)
    flag = True
    while flag:
        try:
            l_vala = float(input("Insira a largura que gostaria de adotar para a vala entre 0.5 m e 1 m:"))
            if (l_vala > 0.5)and(l_vala < 1):
                flag = False
            else:
                print("A largura deve estar entre 0.5 m e 1 m")
        except:
            print("Insira um numero inteiro!")
    print("O campo de absorção da vala de infiltração é de:", "%.2f" % area_abs, "m²")
    c_vala = (area_abs/l_vala)
    print("O comprimento da vala é de:", "%.2f" % c_vala, "m")

    flag = True
    while flag:
        try:
            n_ramais = int(input("Insira o número de ramais:"))
            flag = False
        except:
            print("Insira um numero inteiro")
    tamanho_ramais = c_vala/n_ramais
    print("O tamanho dos ramais é de", "%.2f" % tamanho_ramais, "m")


def modulo_principal():
    """função que recebe as informações principais"""
    try:
        n_contri = int(input("Insira o número de habitantes(no mínimo 5 contribuintes):"))
        if n_contri < 5:
            print("No minimo 5 contribuintes")
            modulo_principal()
    except:
        print("É necessario um numero inteiro")
        modulo_principal()

    padrao = input("Insira o padrão da residência(alto, medio ou baixo):").lower()
    while(padrao != "alto" and padrao != "medio" and padrao != "baixo"):
        print("Padrão inválido")
        padrao = input("Insira o padrão da residência(alto, medio ou baixo):").lower()
    flag = True
    while flag:
        try:
            inter_limp = int(input("Insira o intervalo de limpeza do tanque séptico em anos:"))
            if inter_limp <= 5 and inter_limp >= 1:
                flag = False
            else:
                print("O intervalo de limpeza deve estar entre 1 e 5 anos")
        except:
            print("Insira um numero inteiro!")
    t_amb = float(input("Insira a temperatura ambiente do mês mais frio em ºC:"))
    calculos(n_contri, padrao, inter_limp, t_amb)


def recursividade():
    print("")
    entrada = input("Deseja realizar outro dimensionamento?").lower()
    print("")
    if(entrada == "sim"):
        modulo_principal()
    else:
        print("Muito obrigado por usar o nosso programa")


def calculos(n_contri, padrao, inter_limp, t_amb):
    """função que realiza a analise das informações entradas"""
    # valores de contribuição de despejos e contribuição de lodo, nessa ordem
    dic_padrao = {"alto": [160, 1], "medio": [130, 1], "baixo": [100, 1]}
    contri_despejos = dic_padrao[padrao][0]
    contri_lodo = dic_padrao[padrao][1]
    # tempo de acumulação de acordo com a temperatura
    dic_interlimp = {1: [94, 65, 57], 2: [134, 105, 97], 3: [174, 145, 137], 4: [214, 185, 177], 5: [254, 225, 217]}
    lista_acumulacao = dic_interlimp[inter_limp]
    if(t_amb < 10):
        t_acumulacao = lista_acumulacao[0]
    elif(10 <= t_amb <= 20):
        t_acumulacao = lista_acumulacao[1]
    elif(t_amb > 20):
        t_acumulacao = lista_acumulacao[2]

    contri_diaria = (n_contri*contri_despejos)

    if(contri_diaria < 1500):
        p_retencao = 1
    elif(1501 <= contri_diaria <= 3000):
        p_retencao = 0.92
    elif(3001 <= contri_diaria <= 4500):
        p_retencao = 0.83
    elif(4501 <= contri_diaria <= 6000):
        p_retencao = 0.75
    elif(6001 <= contri_diaria <= 7500):
        p_retencao = 0.67
    elif(7501 <= contri_diaria <= 9000):
        p_retencao = 0.58
    elif(contri_diaria > 9000):
        p_retencao = 0.5

    vol_m3 = (tanque_septico(n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao)/1000)

    if(vol_m3 < 6):
        p_minima, p_maxima = 1.2, 2.2
    elif(6 <= vol_m3 <= 10):
        p_minima, p_maxima = 1.5, 2.5
    elif(vol_m3 > 10):
        p_minima, p_maxima = 1.8, 2.8

    print("O volume útil do tanque séptico prismático é de",\
          "%.2f" % tanque_septico(n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao), "L ou", end=" ")
    print("%.2f" % vol_m3, "m³")
    h_tanque = float(input("Insira a altura que gostaria de adotar para o tanque séptico entre \
%.2f m e %.2f m:" % (p_minima, p_maxima)))
    while(p_minima > h_tanque)or(p_maxima < h_tanque):
        print("A altura deve estar entre %.2f m e %.2f m" % (p_minima, p_maxima))
        h_tanque = float(input("Insira a altura que gostaria de adotar para o tanque séptico entre \
%.2f m e %.2f m:" % (p_minima, p_maxima)))
    dimensoes_tanque(vol_m3, h_tanque)
    print("")
    filtro_anaerobio(n_contri, contri_despejos, p_retencao)
    print("")
    c_infil = float(input("Insira o coeficiente de infiltração do sumidouro em L/m²xdia:"))
    while(c_infil <= 0):
        print("O coeficiente de infiltração deve ser maior que zero")
        c_infil = float(input("Insira o coeficiente de infiltração do sumidouro em L/m²xdia:"))
    sumidouro(c_infil, n_contri, contri_despejos, contri_lodo, p_retencao, t_acumulacao)
    print("")
    vala_infil(contri_diaria, c_infil)
    recursividade()


print("Seja muito bem-vindo ao programa de dimensionamento de sistema de tratamento de esgoto residencial")

# main
modulo_principal()
