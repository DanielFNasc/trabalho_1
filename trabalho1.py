from turtle import *
import tkinter as tk
from tkinter import ttk

TAMANHO_LINHA_CIMA = 20
TAMANHO_BIT = 20

def desenha_eixos():
    largura = 600
    altura = 300

    # eixo x
    setheading(0)
    teleport(-(largura/2), 0)
    color("blue")
    forward(largura)
    stamp()

    # eixo y
    teleport(0, -(altura/2))
    setheading(90)
    forward(altura)
    stamp()
    setheading(0)
    
    teleport(0,0)
    
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

def criar_interface():
    global entrada_bits, combo_metodo
    
    canvas = wn.getcanvas()
    root = canvas.master # Acesso ao Tkinter puro
    
    # Pega altura para posicionar no topo
    altura = wn.window_height()
    largura = window_width()
    y_pos = -(altura / 2) + 40 
    x_pos = -(largura / 2) + 150

    # input bits usuário
    entrada_bits = tk.Entry(root)
    entrada_bits.insert(0, "01011011") 
    canvas.create_window(x_pos, y_pos, window=entrada_bits)
    x_pos += 150

    # combobox opção codificação
    # QUANDO FOREM ADICIONAR CODIFICAÇÃO NOVA TEM QUE ADICIONAR AQUI NO COMBOBOX
    opcoes = ["NRZ-L", "NRZ-I", "AMI", "Pseudoternário", "Manchester", "Manchester_dif", "MLT-3"] #!!!!!!!!!!!!!!!
    combo_metodo = ttk.Combobox(root, values=opcoes, state="readonly")
    combo_metodo.set("NRZ-L")
    canvas.create_window(x_pos, y_pos, window=combo_metodo)
    x_pos += 150

    # botão atualizar
    btn = tk.Button(root, text="Atualizar Gráfico", command=atualizar_grafico)
    canvas.create_window(x_pos, y_pos, window=btn)

def atualizar_grafico():
    sequencia = entrada_bits.get()
    metodo = combo_metodo.get()
    
    clear()
    tracer(0)
    hideturtle()
    
    desenha_eixos()
    
    # QUANDO FOREM ADICIONAR CODIFICAÇÃO NOVA TEM QUE ADICIONAR AQUI NO DICIONÁRIO!!!!!!!!!!!
    # dicionário
    funcoes = {
        "NRZ-L": NRZ_L,
        "NRZ-I": NRZ_I,
        "AMI": AMI,
        "Pseudoternário": pseudoternario,
        "Manchester": Manchester,
        "Manchester_dif": Manchester_dif,
        "MLT-3": MLT_3
    }
    
    # garante que ta no 0,0 antes de começar a codificação
    teleport(0,0)
    setheading(0)
    
    if metodo in funcoes:
        funcoes[metodo](sequencia)
        
    update()

# MAIN 
wn = Screen()

# Isso desativa as atualizações da tela
wn.tracer(0)
hideturtle()

home()
    
criar_interface()
    
atualizar_grafico()

# Mantenha a janela aberta
wn.mainloop()