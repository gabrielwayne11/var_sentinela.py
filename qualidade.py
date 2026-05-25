#Multiplas Funções -- exercicio Controle de Qualidade--
def cabecalho ():
    print("in"+ "=" *30)
    print ("sistema de Qualidade")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
       return "Aprovada"
    else:
       return "Reprovada"
cabecalho()
peso_item = float(input("Digite o peso do item em Gramas:"))
status = verificar_status(peso_item)
print (f"resultado da inspeção:{status}")
print("=" *30)