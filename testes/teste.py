# codigo = input("Informe o seu cupom: ")
#print("o cupom que voce digitou foi: ", codigo)

# if codigo == "FUCTURA1":
#     print("voce ganhou 15% de desconto")
# elif codigo == "FUCTURA2":
#     print("voce ganhou 10% de desconto")
#     print("cupom invalido")





lista_times = []
lista_times_removidos = []

time_digitado = input("digite o nome do time: ")
lista_times.append(time_digitado)
print('lista: ', lista_times)

removido = lista_times.pop()

lista_times_removidos.append(removido)

print('removido: ', removido, '\n', 'lista: ', lista_times_removidos)
print(lista_times)

# print('lista completa: ',lista_times)
# lixeira = lista_times.pop()
# print('removi: ', lixeira,'\n', "lista completa: ",lista_times)