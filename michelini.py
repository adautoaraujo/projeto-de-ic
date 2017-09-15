if(cpf=="micheline")and(senha=="micheline"):
    print("seja bem-vinda Micheline")
    numero_de_parcelas=int(input("Insira o numero de parcelas:"))
    total_familia=0
    total_especies=0
    total_individuos=0
    for i in range(1,numero_de_parcelas+1,1):
        numero_familia=int(input("Insira a quantidade total de familias na parcela:"))
        numero_especie=int(input("Insira a quantidade total de especies na parcela:"))
        numero_individuos=int(input("Insira a quantidade total de individuos na parcela:"))
        total_familia+=numero_familia
        total_especies+=numero_especie
        total_individuos+=numero_individuos
        """for i in range(1,numero_familia+1,1):
            nome_familia=input("Qual o nome da familia?")
        for i in range(1,numero_especie+1,1):
            nome_especie=input("Qual o nome da especie?")
        for i in range(1,numero_individuos+1,1):
            
    area_total=int(input("qual a area total trabalhada:"))
    def dimensionamento():
        dimensionamento=(area_total*total_individuos)/100
        print("total de individuos:",total_individuos)
        """
