def levantamento():
    tamanho_parcela=float(input("Qual o tamanho da parcela em m²?"))
    quant_parcela=int(input("Qual a quantidade de parcelas?"))
    DAP_minima=float(input("Qual a DAP minima considerada em cm?"))
    for i in range(1,quant_parcela+1,1):
        quant_individuos=int(input("Quantos individuos tem na parcela %s:"%(i)))
        for i in range(1,quant_individuos+1,1):
            coordenadas=list(map(str,input("Insira as coordenadas separadas por um espaço do individuo %s:"%(i)).split()))
            DAP_individuo=float(input("Qual a DAP em cm do individuo %s?"%(i)))
            h_total=float(input("Qual a altura em m do individuo %s?"%(i)))
            h_copa=float(input("Qual a altura em m do inicio da copa do individuo %s?"%(i)))
            largura_copa=float(input("Qual a largura em m da copa do individuo %s?"%(i)))
levantamento()
            
