from turtle import * # desenho
import tkinter as tk # componentes da interface
from tkinter import ttk #combobox

TAMANHO_LINHA_CIMA = 20
TAMANHO_BIT = 20
mapa = {
    -3: 0,
    -1: 1,
     0: 1.5,
     1: 2,
     3: 3
}

escritor = Turtle()
escritor.hideturtle()
escritor.penup()

# FUNÇÕES DA INTERFACE --------------------
def desenha_eixos(x_inicial, metodo):
    global largura
    largura = 345
    altura = 300

    # Título do gráfico
    teleport(x_inicial + 50, 120)
    write(metodo, font=("Arial", 12, "bold"))

    # eixo x 
    setheading(0)
    teleport(x_inicial, 0)
    color("red")
    forward(largura)
    stamp()

    # eixo y 
    teleport(x_inicial, -(altura/2))
    setheading(90)
    forward(altura)
    stamp()
    setheading(0)

    teleport(0,0)
    
    color("black")

def criar_interface():
    global entrada_bits, combo_metodo1, combo_metodo2
    
    canvas = wn.getcanvas()
    root = canvas.master # Acesso ao Tkinter puro
    
    # Pega altura para posicionar no topo
    altura = wn.window_height()
    largura = window_width()
    y_pos = -(altura / 2) + 40 
    x_pos = -(largura / 2) + 150

    # input bits usuário
    entrada_bits = tk.Entry(root)
    entrada_bits.insert(0, "0011011001") # valor inicial
    canvas.create_window(x_pos, y_pos, window=entrada_bits)
    x_pos += 150

    # combobox opção codificação
    # QUANDO FOREM ADICIONAR CODIFICAÇÃO NOVA TEM QUE ADICIONAR AQUI NO COMBOBOX
    opcoes = ["NRZ-L", "NRZ-I", "AMI", "Pseudoternário", "Manchester", "Manchester_dif", "MLT-3", "2B1Q", "RZ"] #!!!!!!!!!!!!!!!
    combo_metodo1 = ttk.Combobox(root, values=opcoes, state="readonly")
    combo_metodo1.set("NRZ-L") # valor inicial na combo
    canvas.create_window(x_pos, y_pos, window=combo_metodo1)
    x_pos += 150

    # combobox 2
    combo_metodo2 = ttk.Combobox(root, values=opcoes, state="readonly")
    combo_metodo2.set("NRZ-I") # valor inicial na combo
    canvas.create_window(x_pos, y_pos, window=combo_metodo2)
    x_pos += 150

    # botão atualizar
    btn = tk.Button(root, text="Atualizar Gráfico", command=atualizar_grafico)
    canvas.create_window(x_pos, y_pos, window=btn)

def linha_vertical_bit(x_pos):
    original_pos = pos()
    teleport(x_pos, 70)
    setheading(270)
    color("pink")
    pendown()
    forward(140)
        
    teleport(original_pos[0], original_pos[1]) # volta para onde tava
    color("black")

def desenha_marcadores(sequencia, x_inicial, metodo):
    penup()
    y_texto = 70
    if(metodo == "2B1Q"):
        for i in range(0, len(sequencia), 2):
        
            par = sequencia[i:i+2]
            x_meio = x_inicial + (TAMANHO_BIT) # escrever bit centralizado
            x_fim = x_inicial + TAMANHO_BIT*2
            
            teleport(x_meio - 5, y_texto)
            color("pink") 
            write(par, font=("Arial", 12, "bold"))

            linha_vertical_bit(x_fim)
            
            x_inicial += TAMANHO_BIT*2
    else: 
        for i, bit in enumerate(sequencia):
            x_meio = x_inicial + (TAMANHO_BIT / 2) # escrever bit centralizado
            x_fim = x_inicial + TAMANHO_BIT
            
            teleport(x_meio - 2, y_texto)
            color("pink") 
            write(bit, font=("Arial", 12, "bold"))

            linha_vertical_bit(x_fim)
            
            x_inicial += TAMANHO_BIT
    
    color("black")
    teleport(0, 0) # volta pro o início para desenhar a onda
    pendown()

def atualizar_grafico():
    global x_grafico_1, x_grafico_2
    x_grafico_1 = -350
    x_grafico_2 = 5
    sequencia = entrada_bits.get()
    metodo1 = combo_metodo1.get()
    metodo2 = combo_metodo2.get()
    
    clear()
    tracer(0)
    hideturtle()
    pensize(1)
    desenha_eixos(x_grafico_1, metodo1)
    desenha_marcadores(sequencia, x_grafico_1, metodo1)
    desenha_eixos(x_grafico_2, metodo2)
    desenha_marcadores(sequencia, x_grafico_2, metodo2)

    # QUANDO FOREM ADICIONAR CODIFICAÇÃO NOVA TEM QUE ADICIONAR AQUI NO DICIONÁRIO!!!!!!!!!!!
    # dicionário
    pensize(2)
    funcoes = {
        "NRZ-L": NRZ_L,
        "NRZ-I": NRZ_I,
        "AMI": AMI,
        "Pseudoternário": pseudoternario,
        "Manchester": Manchester,
        "Manchester_dif": Manchester_dif,
        "MLT-3": MLT_3,
        "2B1Q": m2B1Q,
        "RZ" : RZ
    }
    
    escritor.clear()

    # garante que ta no x1,0 antes de começar a codificação
    teleport(x_grafico_1,0)
    escritor.teleport(x_grafico_1,0)
    escritor.setheading(0)
    escritor.forward(230)
    escritor.setheading(90)
    escritor.forward(100)
    setheading(0)
    
    if metodo1 in funcoes:
        funcoes[metodo1](sequencia)

    # garante que ta no x2,0 
    teleport(x_grafico_2,0)
    escritor.teleport(x_grafico_2,0)
    escritor.setheading(0)
    escritor.forward(230)
    escritor.setheading(90)
    escritor.forward(100)

    setheading(0)
    
    if metodo2 in funcoes:
        funcoes[metodo2](sequencia)
        
    update()


# FUNÇÕES DE CODIFICAÇÃO -----------------------

def NRZ_L(sequencia : str):

    ultimo = '0'
    nivelTotal = 0.0
    transicoes = 0
    # turtle auxiliar para texto
    

    if (sequencia[0]=='0'):
        left(90)
        forward(TAMANHO_LINHA_CIMA)
        ultimo = '0'
        nivelTotal = nivelTotal + 1
    if (sequencia[0]=='1'):
        right(90)
        forward(TAMANHO_LINHA_CIMA)
        ultimo = '1'
        nivelTotal = nivelTotal - 1
        transicoes = transicoes +1
    setheading(0)
    forward(TAMANHO_BIT)


    sequencia = sequencia[1:]

    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            if (ultimo == '1'):
                left(90)
                forward(2*TAMANHO_LINHA_CIMA)
                transicoes = transicoes + 1
            ultimo = '0'
            nivelTotal = nivelTotal + 1

        if (c =='1'):
            if (ultimo == '0'):
                right(90)
                forward(2*TAMANHO_LINHA_CIMA)
                transicoes = transicoes + 1
            ultimo = '1'
            nivelTotal = nivelTotal - 1
        
        setheading(0)
        forward(TAMANHO_BIT)
    

    nivelTotal = nivelTotal /(len(sequencia)+1)
    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )

def NRZ_I(sequencia : str):

    nivelTotal = 0.0
    transicoes = 0
    direcao = 1
    setheading(90)
    forward(TAMANHO_LINHA_CIMA)
    for c in sequencia: 
        setheading(0)

        if (c =='1'):
            right(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            direcao = -direcao
            transicoes = transicoes + 1
        nivelTotal = nivelTotal + direcao
        setheading(0)
        forward(TAMANHO_BIT)

    nivelTotal = nivelTotal/ len(sequencia)
    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )
    

def AMI(sequencia :str):
    nivelTotal = 0.0
    transicoes = 0
    direcao = 1
    for c in sequencia: 
        setheading(0)
        if (c =='1'):
            transicoes = transicoes + 2
            left(90*direcao)
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT)
            right(90*direcao)
            forward(TAMANHO_LINHA_CIMA) 
            nivelTotal = nivelTotal + direcao  
            direcao = -direcao
            continue 
        setheading(0)
        forward(TAMANHO_BIT)

    nivelTotal = nivelTotal/ len(sequencia)
    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )
        

def pseudoternario(sequencia :str):
    nivelTotal = 0.0
    transicoes = 0
    direcao = 1
    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            transicoes = transicoes + 2
            left(90*direcao)
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT)
            right(90*direcao)
            forward(TAMANHO_LINHA_CIMA)
            nivelTotal = nivelTotal + direcao    
            direcao = -direcao
            continue 
        setheading(0)
        forward(TAMANHO_BIT)

    nivelTotal = nivelTotal/ len(sequencia)
    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )
       

def Manchester(sequencia : str):
    transicoes = 0
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
    transicoes += 1
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
            transicoes += 1

        #primeira metade horizontal
        setheading(0)
        forward(TAMANHO_BIT/2)

        #transição obrigatória no meio
        right(90*direcao)
        forward(2*tamanho_vertical)
        transicoes += 1
        direcao = -direcao

        #segunda metade horizontal
        setheading(0)
        forward(TAMANHO_BIT/2)

        ultimo_bit = c

    escritor.write(
        f"Nivel medio: {0:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )

def Manchester_dif(sequencia : str):
    transicoes = 0
    direcao = -1
    setheading(90)
    forward(TAMANHO_LINHA_CIMA)
    for c in sequencia: 
        setheading(0)
        if (c =='0'):
            left(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            transicoes += 1
            setheading(0)
            forward(TAMANHO_BIT/2)
            right(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            transicoes += 1
            setheading(0)
            forward(TAMANHO_BIT/2)  
        if (c =='1'):
            setheading(0)
            forward(TAMANHO_BIT/2)
            left(90*direcao)
            forward(2*TAMANHO_LINHA_CIMA)
            transicoes += 1
            setheading(0)
            forward(TAMANHO_BIT/2)  
            direcao = -direcao #apenas o 1 altera

    escritor.write(
        f"Nivel medio: {0:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )


def MLT_3(sequencia :str):
    transicoes = 0
    nivelTotal = 0.0
    nivelAtual = 0
    lastNonZero = -1
    for c in sequencia: 
        if (c == '1' and nivelAtual != 0):
            right(90*lastNonZero)
            forward(TAMANHO_LINHA_CIMA)
            nivelAtual = 0
            transicoes = transicoes + 1
        elif (c == '1' and nivelAtual == 0):
            lastNonZero = -lastNonZero
            left(90*lastNonZero)
            forward(TAMANHO_LINHA_CIMA)
            nivelAtual = lastNonZero
           
            transicoes = transicoes + 1
        setheading(0)
        forward(TAMANHO_BIT)
        nivelTotal = nivelTotal + nivelAtual

    nivelTotal = nivelTotal/ len(sequencia)
    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )
      

def m2B1Q(sequencia :str):
    transicoes = 0
    nivelTotal= 0.0
    nivelAtual = 0
    nivelAnterior = 0
    tamanho2bit = TAMANHO_BIT * 2
    for i in range(0, len(sequencia), 2):
        setheading(0)
        par = sequencia[i:i+2]

        # guarda o nível anterior antes de atualizar
        nivelAnterior = nivelAtual

        # escolhe novo nível dependendo do sinal do nível anterior (lógica original preservada)
        if nivelAnterior >= 0:
            if par == '00':
                nivelAtual = 1
            elif par == '01':
                nivelAtual = 3
            elif par == '10':
                nivelAtual = -1
            elif par == '11':
                nivelAtual = -3
        else:
            if par == '00':
                nivelAtual = -1
            elif par == '01':
                nivelAtual = -3
            elif par == '10':
                nivelAtual = 1
            elif par == '11':
                nivelAtual = 3

        
    
        posAnterior = mapa[nivelAnterior]
        posAtual = mapa[nivelAtual]

        diferenca = posAtual - posAnterior
        nivelTotal = nivelTotal + nivelAtual
        distancia = diferenca* TAMANHO_LINHA_CIMA
        if diferenca == 0:
            # sem transição vertical, apenas avancar
            setheading(0)
            forward(tamanho2bit)
            continue
            

        # distância vertical absoluta
        
        # direção da transição: >0 = subir, <0 = descer
        elif diferenca > 0:
            # sobe: gira para cima (left 90), move, avança, volta para baixo
            left(90)
            forward(distancia)
            setheading(0)
            forward(tamanho2bit)
           
        elif diferenca < 0:
            # desce: gira para baixo (right 90), move, avança, volta para cima
            left(90)
            forward(distancia)
            setheading(0)
            forward(tamanho2bit)

        if(nivelAtual != nivelAnterior and nivelAnterior!=0):
            transicoes = transicoes + 1
        
        
        nivelAnterior = nivelAtual
    print(f"nivel total final {nivelTotal}")
    nivelTotal = nivelTotal/ len(sequencia)

    escritor.write(
        f"Nivel medio: {nivelTotal:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )
        
def RZ(sequencia: str):
    transicoes = 0
    nivelTotal = 0.0

    for c in sequencia:
        setheading(0)
        
        if c == '1':
            left(90) # sobe
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT / 2) # desenha metade
            right(90) # desce
            forward(TAMANHO_LINHA_CIMA)
            transicoes += 2  # uma subida e uma descida
            nivelTotal += 0.5 # +1V por metade do tempo
        else:
            right(90) # desce
            forward(TAMANHO_LINHA_CIMA)
            setheading(0)
            forward(TAMANHO_BIT / 2) # desenha metade do bit
            left(90) # sobe
            forward(TAMANHO_LINHA_CIMA)
            transicoes += 2  # uma descida e uma subida
            nivelTotal -= 0.5 # -1V por metade do tempo
        
        # desenha a segunda metade do bit no eixo zero
        setheading(0)
        forward(TAMANHO_BIT / 2)

    # cálculo da média final
    nivelMedio = nivelTotal / len(sequencia)

    # escrita
    escritor.write(
        f"Nivel medio: {nivelMedio:.2f}\nTransicoes: {transicoes}",
        align="left",
        font=("Arial", 12, "normal")
    )



# MAIN ----------------
wn = Screen()

# Isso desativa as atualizações da tela
wn.tracer(0)
hideturtle()

home()
    
criar_interface()
    
atualizar_grafico()

# Mantenha a janela aberta
wn.mainloop()