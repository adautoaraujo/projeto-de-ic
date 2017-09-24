def vala_de_infiltracao(): #sistema de escoamento por tubos
    n_contri= int(input("Insira o número de contribuintes:")) #numero de habitantes
    contri_diaria= float(input("Insira a contribuicao em L/hab*dia:"))#contribuicao de cada habitante
    c_infiltracao= float(input("Insira o coeficiente de infiltracao L/m²*dia:")) #coeficiente de infiltracao
    v_contri= (n_contri * contri_diaria) #volume de contribuicao L/dia
    l_vala= float(input("Insira a largura da vala em m:")) #largura vala
    n_ramais=int(input("Insira o numero de ramais:")) #numero de ramais do sistema
    a_infiltracao= (v_contri/c_infiltracao)
    print("A área de infiltracao da vala é de:",a_infiltracao,"m²")
    c_vala= (a_infiltracao/l_vala) #comprimento vala
    print("O comprimento da vala é de:",c_vala,"m")
    t_ramais= (c_vala/n_ramais) #tamanho dos ramais
    print("O tamanho dos ramais é de:",t_ramais,"m")
vala_de_infiltracao()
    
    
