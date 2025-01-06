lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]                                                                            #criação de listas


lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]                                                               #percorrer os elementos de uma lista com for
for numero in lista_de_numeros:
    print(numero)


soma_impares = 0                                                                                           #calcular a soma dos intens de uma lista
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)



for i in range(10, 0, -1):                                                                          #imprimir os itens da lista de forma decrescente
    print(i)