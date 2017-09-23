def vu_tanque_septico():
        n_contri= int(input("Insira o numero de contribuintes:")) #num contribuintes
	contri_diaria= float(input("Insira a contribuicao de despejos em litros/pessoa por dia:")) #litros por pessoa
	t_retencao= float(input("Insira o período de detenção em dias:")) #período de detecao em dias
	taxa_acum= float(input("Insira a taxa de acumulação de logo digerido em dias:")) #taxa de acumulação de lodo digerido em dias
	contri_lodo= float(input("Insira a contribuicao de lodo fresco em litro/pessoa por dia:")) #contribuicao de lodo em litros por pessoa
	volume_util= 1000 + n_contri*((contri_diaria*t_retencao)+(taxa_acum*contri_lodo)) #calculo do volume util do tanque
	print("O volume do tanque séptico é de:",volume_util,"L")
vu_tanque_septico()

