import tkinter as tk

janela  =  tk.Tk()
janela.geometry('500x500')
janela.title('Isso é uma Janela')

def soma():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    soma  =  n1  + n2
    resultado.config(text=f'Resultado {int(soma)}')


def sub():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    sub  =  n1  - n2
    resultado.config(text=f'Resultado {int(sub)}')

def div():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    div  =  n1  // n2
    resultado.config(text=f'Resultado {div}')

def mult():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    mult  =  n1  - n2
    resultado.config(text=f'Resultado {mult}')


text_label =  tk.Label(janela, text='CALCULADORA', fg = 'black', bg='white')
text_label.pack()


input_entry1 = tk.Entry(janela, width = 5)
input_entry1.pack()

input_entry2 = tk.Entry(janela, width = 5)
input_entry2.pack()


btn_soma  = tk.Button(janela, text= '+', command = soma, fg='white', bg='black')
btn_soma.pack()  

btn_sub  = tk.Button(janela, text= '-', command = sub, fg='white', bg='black')
btn_sub.pack()  

btn_div  = tk.Button(janela, text= '/', command = div, fg='white', bg='black')
btn_div.pack()  

btn_mult  = tk.Button(janela, text= '*', command = mult, fg='white', bg='black')
btn_mult.pack()  

resultado =  tk.Label(janela, text='Resultado')
resultado.pack()

janela.mainloop()