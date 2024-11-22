# and  ( da veraddeiro quando os dois elementos é correta e falso quando alguma esta incorreto)
# or   ( é quando qualquer uma for verdadeira da true, caso todas as duas de falso ai é falso)
# not  ( inverte o verdadeiro para falsoo e o falso para verdadeiro)

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print (exp_3)