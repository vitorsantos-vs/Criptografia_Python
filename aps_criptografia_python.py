#Criptografia

def cifra(mesagem, direcao):    #definição que pede a mensagem e a direção( + ou - ) para somar ou subtrair as letras
    ALFABETO =  "abcdefghijklmnopqrstuvwxyz"    #alfabeto brasileiro
    linha_divisão()
    KEY = int(input("insira uma Chave (1 até 25): "))  #solicitar uma chave de 1 até 25 para fazer a troca das letras
    linha_divisão()
    if(KEY < 1 or KEY > 25):    #verivica se a chave estã dentro do estabelecido para a criptografia funcionar sem erro
        print("*Opção Invalida*")    
        exit()  #se entra na condição da chave, passa a mensagem de erro e sai do programa

    msg = " "   #recebe a mensagem vazia para fazer a substituição
    for c in mesagem:
        if c in ALFABETO:   #verifica de o caracter está no alfabeto
            c_index = ALFABETO.index(c)
            msg += ALFABETO[(c_index + (direcao * KEY)) % len(ALFABETO)]    #se o caracter estiver, ele pega o caracter e soma ou subtrair a letra
        else:
            msg += c    #se não tiver no alfabeto ele concatena e ignora a posição dele

    return msg  #retona a mensagem que foi inserida         

def criptografar(mensagem):     #onde ele verifica se é + para criptografar
    return cifra(mensagem, 1)

def descriptografar(mensagem):      #onde ele verifica se é - para descriptografar
    return cifra(mensagem, -1)

def main():
    linha_divisão()
    comando = input("Digite o comando [1]criptografar ou [2]descriptografar\ncomando: ")    #solita o camando de criptografia e descriptografia

    linha_divisão()
    mensagem = input("Digite a mensagem: ")     #solicita a mensagem

    if comando == '1':  #valista a criptografia
        print(criptografar(mensagem))
    elif comando == '2':    #valida a descriptografia
        print(descriptografar(mensagem))
    else:   #caso o comando seja diferente do solicidado
        print(comando + "*Comando invalido*")
        exit()

    continuação()   #solicita a continuação ou o fim do programa

def continuação():
    linha_divisão()
    print("Deseja Continuar? (sim) (nao) ")    #solicitação de continuação

    escolha = str(input("Sua escolha: "))
    if escolha == "sim":    #valida se continua
        return main()
    elif escolha == "nao":  #valida se encerra o programa
        linha_divisão()
        print("Fim do Programa")
    else:   #caso o comando seja diferente do solicidado
        linha_divisão()
        print("*Opção Invalida*")

def linha_divisão():    #traçar uma linha para melhor visualização do programa
    print("=+=" * 17)

if __name__ == '__main__':  #onde chama a função para inicia o programa.
    main()  