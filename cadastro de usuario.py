cpf=input()
senha=input()
if(cpf=="mateus")and(senha=="mateus"):
    print("Seja bem-vindo Mateus")
    novo_usuario=input("Insira o primeiro nome do novo usuario:")
    cpf_usuario=input("Insira os numeros do cpf do usuario:")
    while(len(cpf_usuario)!=11):
        print("Cpf invalido")
        cpf_usuario=int(input("Insira o cpf do usuario sem espaços ou separadores:"))
    senha_usuario=int(input("Insira senha numerica de 6 digitos:"))
    while(len(senha_usuario)!=6):
        print("Senha invalida")
        senha_usuario=int(input("Insira senha numerica de 6 digitos:"))
