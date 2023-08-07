def exibirConteudo():
    arquivo = open('numbers.txt')
    
    conteudo = arquivo.read()

    numeros = conteudo.split(',')

    for numero in numeros:
        print(numero)
            
    arquivo.close()

if __name__ == '__main__':
    exibirConteudo()