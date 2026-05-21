n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
opcr=input("escolha a operaçao +,-,/,*: ")
if opcr=="+":
    resultado1=n1+n2
    print(resultado1)
elif opcr=="-":
    resultado2=n1-n2
    print(resultado2)
elif opcr=="*":
    resultado3=n1*n2
    print(resultado3)
elif opcr=="/":
    resultado4=n1/n2
    print(resultado4)
else:
    print("erro opçao indisponivel")