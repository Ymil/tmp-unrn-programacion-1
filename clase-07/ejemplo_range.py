# for x in range(0, 3):
#     print(x)

lista = [-11, 2, 3, 10, 50, 100]

lista[-1] # Agarro el ultimo elemento de la lista

# Forma 1 de recorrer una lista
# for elemento_indice in range(0, len(lista)):
#     print(elemento_indice, " - ", lista[elemento_indice])

# Forma 2 de recorrer listas
idx = 0
for elemento in lista:
    print(idx, " - " ,elemento)
    idx += 1