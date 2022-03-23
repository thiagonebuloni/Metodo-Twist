#!/usr/bin/env python
# coding: utf-8

# In[20]:


def main():
    """
    Criptografia de strings via método de substituição (Twist). v2022-1.0
    
    Essa versão do programa considera apenas os caracteres '_', '.' e 'a...z', todos em lower case.
    
    A função menu() apresenta o programa e as opções: 0 para codificar uma mensagem, e 1 para decodificar.
    Chama as funções codificador() e decodificador().
    
    Baseado em um trabalho pedido em cursos da USP pelo Departamento de Ciência da
    Computação (DCC).
    """
    while True:
        print()
        print("Codificador / decodificador de texto")
        print()
        print("Digite 0 para codificar e 1 para decodificar")
        print("e qualquer outro número para sair: ", end='')
        escolha = int(input())
        
        if escolha == 0:
            print(f"Frase final: {codificador()}")
        elif escolha == 1:
            print(f"Frase final: {decodificador()}")
        else:
            break
    
    
    
def codificador():
    '''
    :return: String criptografada
    Função que recebe a chave, a mensagem e a retorna criptografada.
    '''
    codigo_plano = []
    cifra_do_codigo = []
    cifra_do_codigo_final = []
    frase_final = ''
    
    k = int(input("Digite a chave: "))
    texto_plano = str(input("Digite a mensagem: "))
    
    # substitui espaço por _
    texto_plano2 = texto_plano.replace(' ','_')
    
    # converte caracteres para números
    for i in range(len(texto_plano2)):
        codigo_plano.append(char_2_Num(texto_plano2[i]))
    
    # fórmula da cifra
    for i in range(len(texto_plano2)):
        cifra_do_codigo.append((codigo_plano[(k * i) % len(texto_plano2)] - i) % 28)
    
    # reconverte números em caracteres
    for i in range(len(cifra_do_codigo)):
        cifra_do_codigo_final.append(num_2_Char(cifra_do_codigo[i]))
        
    # cria uma string frase_final com o resultado da conversao para apresentação.
    for i in range(len(cifra_do_codigo_final)):
        frase_final += cifra_do_codigo_final[i]
        
    return frase_final


def decodificador():
    '''
    Função que recebe a chave, a mensagem e a retorna descriptografada.
    :return: String descriptografada
    '''
    cifra_do_codigo = []
    cifra_do_codigo_final = []
    texto_plano = []
    frase_final = ''
    
    k = int(input("Digite a chave: "))
    cifra_do_codigo_final = str(input("Digite a mensagem: "))
    codigo_plano = [0] * len(cifra_do_codigo_final)

    # converte caracteres para números
    for i in range(0, len(cifra_do_codigo_final)):
        cifra_do_codigo.append(char_2_Num(cifra_do_codigo_final[i]))
    
    # fórmula da cifra
    n = len(cifra_do_codigo)
    for i in range(0, n):
        codigo_plano[(k * i) % len(cifra_do_codigo)] = ((cifra_do_codigo[i] + i) % 28)
    
    # reconverte números em caracteres
    for i in range(0, len(codigo_plano)):
        texto_plano.append(num_2_Char(codigo_plano[i]))
        
    # cria uma string frase_final com o resultado da conversão para apresentação.
    for i in range(0, len(texto_plano)):
        frase_final += texto_plano[i]
    
    # substitui _ por espaco
    frase_final = frase_final.replace('_',' ')
    
    return frase_final


def char_2_Num(caractere):
    '''
    :param caractere: caractere alfabético
    :return: int
    Função que recebe um caractere e converte em um correspondente numérico
    '''
    dic = {"_" : 0, "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11,
          "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22,
          "w" : 23, "x" : 24, "y" : 25, "z" : 26, "." : 27}
    return dic[caractere]


def num_2_Char(numero):
    '''
    :param numero: número inteiro
    :return: char
    Função que recebe um número e converte em um correspondente alfabético
    '''
    dic = {0 : "_", 1 : "a", 2 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h", 9 : "i", 10 : "j", 11 : "k",
          12 : "l", 13 : "m", 14 : "n", 15 : "o", 16 : "p", 17 : "q", 18 : "r", 19 : "s", 20 : "t", 21 : "u", 22 : "v",
          23 : "w", 24 : "x", 25 : "y", 26 : "z", 27 : "."}  
    return dic[numero]


if __name__ == '__main__':
    main()

