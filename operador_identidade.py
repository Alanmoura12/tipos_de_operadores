saldo = 1000
limite = 500

print (saldo is limite)  # se o objeto ocupam mesma memoria, se sim da true
print (saldo is not limite) # inverte 

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200


print (curso is nome_curso)
print (curso is not nome_curso)


print (saldo is limite)
print (saldo is not limite)