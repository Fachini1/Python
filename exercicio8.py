idade = input("Insira sua idade:\n")
idade = int(idade)

    

if (idade <= 12):
    print('Criança')
elif (13< idade < 18):
    print('Adolescente')
elif (idade >= 18):
    print('Adulto')
else:
    print('Valor Invalido')
    