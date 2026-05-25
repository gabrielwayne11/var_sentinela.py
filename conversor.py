#ferramenta de conversão Dólar x Real --
def converter(valor_dobr):
    taxa  = 5.15
    valor_real =  valor_dobr * taxa
    return valor_real
print ("Conversar dólar x real")
preco = float(input("Digite o preço do produto em Dólar:" ))
resultado = converter(preco)
print(f" o Valor em reais é: {resultado:.2f}")