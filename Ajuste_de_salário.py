salario = float (input("Informe o seu salário:" ))

if salario < 128000:
                percentagem = 0.2
                aumento = salario * 0.2
                resultado= salario + aumento
                                
                 
elif salario >= 128000 and salario <= 500000:
                percentagem = 0.15
                aumento = salario * percentagem
                resultado= salario + aumento
               
elif salario >= 500000 and salario <= 1000000:
                percentagem = 0.1
                aumento = salario * 0.1
                resultado= salario + aumento
               
else:
    percentagem = 0.05
    aumento = salario * 0.05
    resultado= salario + aumento
   
print("Salário antes do reajuste", salario)
print("Percentagem:",percentagem)
print("Valor do aumento:", aumento)
print("Novo salário:", resultado)
                 
