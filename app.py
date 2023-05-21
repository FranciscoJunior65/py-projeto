def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc < 24.9:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
peso = float(input("Informe o seu peso (em kg):"))
altura = float(input("Informe a sua altura em metros): "))

imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

print("seu IMC é: {:.2f}".format(imc))
print("Categoria: {}".format(categoria))