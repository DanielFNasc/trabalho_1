from turtle import *

TAMANHO_LINHA_CIMA = 20
TAMANHO_BIT = 20

def desenha_eixos(sequencia : str):

    #eixo horizontal
    for c in sequencia:
        color("blue")
        forward(TAMANHO_BIT*len(sequencia))
    teleport(0)
    color("black")

def NRZ_L(sequencia : str):

    ultimo = '0'

    if (sequencia[0]=='0'):
        left(90)
        forward(TAMANHO_LINHA_CIMA)
        ultimo = '0'
    if (sequencia[0]=='1'):
        right(90)
        forward(TAMANHO_LINHA_CIMA)
        ultimo = '1'
    
    setheading(0)
    forward(TAMANHO_BIT)


    sequencia = sequencia[1:]
    print(sequencia)
    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            if (ultimo == '1'):
                left(90)
                forward(2*TAMANHO_LINHA_CIMA)
            ultimo = '0'

        if (c =='1'):
            if (ultimo == '0'):
                right(90)
                forward(2*TAMANHO_LINHA_CIMA)
            ultimo = '1'
        
        setheading(0)
        forward(TAMANHO_BIT)

def NRZ_I(sequencia : str):

    direcao = 1
    setheading(90)
    forward(TAMANHO_LINHA_CIMA)
    for c in sequencia: 
        setheading(0)
        if (c =='1'):
            right(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            direcao = -direcao
        setheading(0)
        forward(TAMANHO_BIT)
    

def AMI(sequencia :str):
    direcao = 1
    for c in sequencia: 
        setheading(0)
        if (c =='1'):
            left(90*direcao)
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT)
            right(90*direcao)
            forward(TAMANHO_LINHA_CIMA)   
            direcao = -direcao
            continue 
        setheading(0)
        forward(TAMANHO_BIT)

def pseudoternario(sequencia :str):
    direcao = 1
    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            left(90*direcao)
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT)
            right(90*direcao)
            forward(TAMANHO_LINHA_CIMA)   
            direcao = -direcao
            continue 
        setheading(0)
        forward(TAMANHO_BIT)

def Manchester(sequencia : str):

    tamanho_vertical = TAMANHO_LINHA_CIMA

    ultimo_bit = sequencia[0]

    # 1 = cima
    # -1 = baixo

    #desenha o primeiro bit
    if (ultimo_bit == '0'):
        direcao = 1

    else:
        direcao = -1

    left(90*direcao)
    forward(tamanho_vertical)

    setheading(0)
    forward(TAMANHO_BIT/2)

    right(90*direcao)
    forward(2*tamanho_vertical)

    direcao = -direcao

    setheading(0)
    forward(TAMANHO_BIT/2)

    #começa a partir da segunda posição
    sequencia = sequencia[1:]

    for c in sequencia:

        #bits iguais, precisa transição no começo
        if (ultimo_bit == c):
            direcao = -direcao #inverte a direção
            left(90*direcao)
            forward(2*tamanho_vertical)

        #primeira metade horizontal
        setheading(0)
        forward(TAMANHO_BIT/2)

        #transição obrigatória no meio
        right(90*direcao)
        forward(2*tamanho_vertical)

        direcao = -direcao

        #segunda metade horizontal
        setheading(0)
        forward(TAMANHO_BIT/2)

        ultimo_bit = c

def Manchester_dif(sequencia : str):
    direcao = -1
    setheading(90)
    forward(TAMANHO_LINHA_CIMA)
    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            left(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT/2)
            right(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT/2)  
        if (c =='1'):
            setheading(0)
            forward(TAMANHO_BIT/2)
            left(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT/2)  
            direcao = -direcao #apenas o 1 altera


def MLT_3(sequencia :str):
    nivelAtual = 0
    lastNonZero = -1
    for c in sequencia: 
        if (c == '1' and nivelAtual != 0):
            right(90*lastNonZero)
            forward(TAMANHO_LINHA_CIMA)
            nivelAtual = 0
        elif (c == '1' and nivelAtual == 0):
            lastNonZero = -lastNonZero
            left(90*lastNonZero)
            forward(TAMANHO_LINHA_CIMA)
            nivelAtual = lastNonZero
        setheading(0)
        forward(TAMANHO_BIT)
    pass

#sequencia = input("Qual a dequencia de bits? ")
sequencia = "010011"


wn = Screen()

# Isso desativa as atualizações da tela
wn.tracer(0)

home()
desenha_eixos(sequencia)
home()
#NRZ_L(sequencia)
#NRZ_I(sequencia)
#AMI(sequencia)
#pseudoternario(sequencia)
Manchester(sequencia)
#Manchester_dif(sequencia)
#MLT_3(sequencia)


# Atualize a tela para ver as mudanças
wn.update()

# Mantenha a janela aberta
wn.mainloop()



