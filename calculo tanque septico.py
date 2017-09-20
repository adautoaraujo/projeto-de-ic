def vu_tanque_septico(): #
	n_contri= int(input()) #num contribuintes
	contri_diaria= float(input()) #litros por pessoa
	t_retencao= float(input()) #período de detecao em dias
	taxa_acum= float(input()) #taxa de acumulação de lodo digerido em dias
	contri_lodo= float(input()) #contribuicao de lodo em litros por pessoa
	volume_util= 1000 + n_contri*((contri_diaria*t_retencao)+(taxa_acum*contri_lodo))
	print("O volume do tanque séptico é de:",volume_util,"L")
vu_tanque_septico()
