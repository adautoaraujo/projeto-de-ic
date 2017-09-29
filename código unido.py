def login():
    cpf=input("Insira seu cpf:")
    senha=input("Insira sua senha:")
    if(cpf=="mateus")and(senha=="mateus"):
        mateus()
    elif(cpf=="antonio")and(senha=="antonio"):
        entrada_dados_antonio()
    elif(cpf=="02306144427")and(senha=="123456"):
        parcela()
def mateus():
    print("Seja bem-vindo Mateus")
    acao=input("O que voce gostaria de fazer: cadastrar ou excluir usuário?").lower()
    while(acao!="cadastrar")and(acao!="excluir"):
        print("Ação inválida")
        acao=input("O que voce gostaria de fazer: cadastrar ou excluir usuário?").lower()
    if(acao=="cadastrar"):
        cadastrar()
    elif(acao=="excluir"):
        excluir()        
def cadastrar():            
    novo_usuario=input("Insira o primeiro nome do novo usuario:").lower()
    cpf_usuario=str(input("Insira o cpf do usuario:"))
    while(len(cpf_usuario)!=11):
        print("Cpf invalido")
        cpf_usuario=str(input("Insira o cpf do usuario sem espaços ou separadores:"))
        if(len(cpf_usuario)==11):
            print("cpf correto")
    senha_usuario=str(input("Insira senha numerica de 6 digitos:"))
    while(len(senha_usuario)!=6):
        print("Senha invalida")
        senha_usuario=str(input("Insira senha numerica de 6 digitos:"))
    print("Usuario cadastrado")
    recursividade()
def excluir():
    cpf_excluir=str(input("Insira o cpf do usuario:"))
    if(len(cpf_excluir)==11):
        while(len(cpf_excluir)!=11):
            print("Cpf invalido")
            cpf_excluir=str(input("Insira o cpf do usuario sem espaços ou separadores:"))
            if(len(cpf_excluir)==11):
                print("Usuario excluido")
        print("Usuario excluido")
    recursividade()
def recursividade():
    continuar=str(input("Deseja continuar administrando usuarios?").lower())
    if(continuar=="sim"):
        mateus()
    else:
        login()
def tanque_septico(n_contri,contri_despejos,contri_lodo,p_retencao,t_acumulacao):
    v_util=(1000+n_contri*((contri_despejos*p_retencao)+(t_acumulacao*contri_lodo)))
    return v_util
def filtro_anaerobio(n_contri,contri_despejos,p_retencao):
    v_util= (1.6*n_contri*contri_despejos*p_retencao)
    return v_util
def dimensoes_filtro(n_contri,contri_despejos,p_retencao):
    print("A altura do leito filtrante é de 1.2m")
    print("A profundidade util do filtro anaerobio é de 1.8m")
    print("Diametro minimo: 0.95m e diametro maximo: 5.4m")
    print("Largura minima: 0.85m e largura maxima: 5.4m")
    print("A area da base do filtro anaerobio é de","%.2f"%(filtro_anaerobio(n_contri,contri_despejos,p_retencao)/1.2),"m²")
    recursividade1()
def entrada_dados_antonio():
    print("Seja bem-vindo Antonio")
    n_contri=int(input("Insira o numero de habitantes:"))
    padrao= input("Insira o padrão da residencia(alto, medio ou baixo):").lower()
    while(padrao!="alto")and(padrao!="medio")and(padrao!="baixo"):
            padrao= input("Insira o padrão da residencia(alto, medio ou baixo):").lower()
            if(padrao=="alto")or(padrao=="medio")or(padrao=="baixo"):
                break
    t_acumulacao = float(input("Insira a taxa de lodo digerido em dias:"))

    if(padrao=="alto"):
        contri_despejos,contri_lodo= 160,1
    elif(padrao=="medio"):
        contri_despejos,contri_lodo= 130,1
    elif(padrao=="baixo"):                                                       
        contri_despejos,contri_lodo= 100,1  
              
    contri_diaria=(n_contri * contri_despejos)
    if(contri_diaria<1500):
        p_retencao=1
    elif(1501<=contri_diaria<=3000):
        p_retencao=0.92
    elif(3001<=contri_diaria<=4500):
        p_retencao=0.83
    elif(4501<=contri_diaria<=6000):
        p_retencao=0.75
    elif(6001<=contri_diaria<=7500):
        p_retencao=0.67
    elif(7501<=contri_diaria<=9000):
        p_retencao=0.58
    elif(contri_diaria>9000):
        p_retencao=0.5
    
    print("O volume util do tanque septico é de",tanque_septico(n_contri,contri_despejos,contri_lodo,p_retencao,t_acumulacao),"L")
    print("O volume util do filtro anaerobio é de",filtro_anaerobio(n_contri,contri_despejos,p_retencao),"L")
    dimensoes_filtro(n_contri,contri_despejos,p_retencao)
def parcela():
    print("Seja bem-vinda Michelline")
    quant_individuos=int(input("Quantos individuos tem na parcela?"))
    informacoes={}
    ab_amostra={}
    ab_parcela=0
    for i in range(1,quant_individuos+1,1):
        info_individuo=list(map(str,input("Insira familia, especie, nome popular, DAP, altura total em m, altura do inicio da copa em m e largura da copa em m separados por um -, do individuo %s:"%(i)).split("-")))
        DAP=str(info_individuo[3])
        informacoes[i]=info_individuo
        import math
        a_basal=(math.pi*(float(DAP))**2)/4
        ab_amostra[i]=a_basal
        ab_parcela+=a_basal
    print("A area basal da parcela é:",ab_parcela)
    recursividade2()
def recursividade1():
    continuar=str(input("Deseja continuar realizando os estudos?").lower())
    if(continuar=="sim"):
        entrada_dados_antonio()
    else:
        login()
def recursividade2():
    continuar=str(input("Deseja continuar calculando parcela?").lower())
    if(continuar=="sim"):
        parcela()
    else:
        login()
login()
