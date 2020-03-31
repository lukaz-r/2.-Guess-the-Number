from random import randint


def numReal(value): #Verifica se o numero é real (falta melhores validações)
    
    if not value.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():  # Tira todos pontos, tacos, espacos e verifica se e um numero
        print("não é um numero")
        return False

        try:
            float(value)

        except ValueError:
            print("Except numReal")
            return False

    #print("E um numero")
    return True


def num_Secreto(): #Sorteia o numero entre 0 e 100
    num_Secreto = 0
    num_Secreto = randint(0, 101)
    return num_Secreto


def verificaEntrada(value, num): # valida valor digitado 
    
    if(value > 100):
        print("Valor maior que o intervalo de sorteio! ")
        return False
    elif(value < 0):
        print("Valor menor que o intervalo de sorteio!")
        return False
    elif(value > num):
        print("O valor sorteado é menor")
        return False
    elif(value < num):
        print("O valor sorteado é maior")
        return False
    elif(value == num):
        print("Parabéns voce acertou")
        print("Miseravi")
        return True
    else:
        print("Erro")
        return False


def joga(): # Seta um valor e começa o jogo
    sorteado = num_Secreto()
    #print(sorteado)
    
    while True:
        numero = 0
        numero = input("Digite o numero sorteado: ")
        if(numReal(numero) == True):
            if(verificaEntrada(float(numero), sorteado) == True):
                break
    print("Fim de jogo!")


def printa(): # Sortea e printa (Para fins de teste)
    print(num_Secreto())
 