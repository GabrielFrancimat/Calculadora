from tkinter import *
from tkinter import ttk
import math

color1 = "#0f0f0f"  # cor Black/Preto
color2 = "#f08502"  # cor Orange/Laranja
color3 = "#78766f"  # cor Brown/Marrom
color4 = "#ffffff"  # cor White/Branco
color5 = "#03e6ff"  # cor Cyan/Ciano
color6 = "#bbc7be"  # cor Gray/Cinza

window = Tk()
window.title("Calculadora-Padrão")
window.geometry("290x420")
window.config(bg=color1)

# Definindo os frames
frame_window = Frame(window, width=290, height=60, bg=color3)
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=290, height=410)
frame_body.grid(row=1, column=0)

# Variável todos valores
all_values = ''

value_text = StringVar()

# Funções para o código

# Função de inserir valores
def input_values(event):
    global all_values

    all_values = all_values + str(event)

    # Mostrando o valor na tela
    value_text.set(all_values)

# Função de calcular
def calculate():
    global all_values

    try:
        result = eval(all_values)
        value_text.set(str(result))
        # Atualiza all_values com o resultado
        all_values = str(result)
    except:
        value_text.set("Erro")
        all_values = ""

# Função de limpar tela
def clear_screen():
    global all_values

    all_values = ""
    value_text.set("")

# Função de remover o último caractere
def clear_last():
    global all_values

    all_values = all_values[:-1]
    value_text.set(all_values)

# Função para calcular 1/x
def calculate_fraction():
    global all_values

    all_values = 1/int(all_values)
    str(all_values)
    value_text.set(all_values)


# Função para calcular raiz de x
def calculate_root():
    global all_values

    all_values = math.sqrt(int(all_values))
    str(all_values)
    value_text.set(all_values)


# Função para trocar o sinal do número
def change_token():
    global all_values

    if all_values:
        try:
            all_values = str(-float(all_values))
            value_text.set(all_values)
        except ValueError:
            value_text.set("Erro")
            all_values = ""


# Criando Label
app_label = Label(frame_window, textvariable=value_text, width=20, height=2,
                  padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=color3)
app_label.place(x=0, y=0)

# Definindo os botões

# Botões de Limpeza
buttom_clear = Button(frame_body, command=clear_screen, text="CE", width=10,
                      height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_clear.place(x=0, y=0)

buttom_clear_last = Button(frame_body, command=clear_last, text="<=", width=20,
                           height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_clear_last.place(x=140, y=0)

# Operações Aritiméticas
buttom_rest = Button(frame_body, command=lambda: input_values('%'), text="%", width=8,
                     height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_rest.place(x=80, y=0)

buttom_fraction = Button(frame_body, command=calculate_fraction, text="1/x", width=9,
                         height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_fraction.place(x=0, y=60)

buttom_square = Button(frame_body, command=lambda: input_values('**'), text="**", width=9,
                       height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_square.place(x=75, y=60)

buttom_square_root = Button(frame_body, command=calculate_root, text="√x", width=9,
                            height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_square_root.place(x=150, y=60)

buttom_division = Button(frame_body, command=lambda: input_values('/'), text="/", width=9,
                         height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_division.place(x=225, y=60)

buttom_multi = Button(frame_body, command=lambda: input_values('*'), text="*", width=9,
                      height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_multi.place(x=225, y=120)

buttom_minus = Button(frame_body, command=lambda: input_values('-'), text="-", width=9,
                      height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_minus.place(x=225, y=180)

buttom_plus = Button(frame_body, command=lambda: input_values('+'), text="+", width=9,
                     height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_plus.place(x=225, y=240)

buttom_minus_or_plus = Button(frame_body, command=change_token, text="+/-", width=9,
                              height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_minus_or_plus.place(x=0, y=300)

buttom_comma = Button(frame_body, command=lambda: input_values('.'), text=".", width=9,
                      height=3, bg=color2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_comma.place(x=150, y=300)

buttom_equal = Button(frame_body, command=calculate, text="=", width=9,
                      height=3, bg=color5, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_equal.place(x=225, y=300)

# Algarismos numéricos
buttom_0 = Button(frame_body, command=lambda: input_values('0'), text="0", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_0.place(x=75, y=300)

buttom_1 = Button(frame_body, command=lambda: input_values('1'), text="1", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_1.place(x=0, y=240)

buttom_2 = Button(frame_body, command=lambda: input_values('2'), text="2", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_2.place(x=75, y=240)

buttom_3 = Button(frame_body, command=lambda: input_values('3'), text="3", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_3.place(x=150, y=240)

buttom_4 = Button(frame_body, command=lambda: input_values('4'), text="4", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_4.place(x=0, y=180)

buttom_5 = Button(frame_body, command=lambda: input_values('5'), text="5", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_5.place(x=75, y=180)

buttom_6 = Button(frame_body, command=lambda: input_values('6'), text="6", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_6.place(x=150, y=180)

buttom_7 = Button(frame_body, command=lambda: input_values('7'), text="7", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_7.place(x=0, y=120)

buttom_8 = Button(frame_body, command=lambda: input_values('8'), text="8", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_8.place(x=75, y=120)

buttom_9 = Button(frame_body, command=lambda: input_values('9'), text="9", width=9,
                  height=3, bg=color6, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
buttom_9.place(x=150, y=120)


window.mainloop()
