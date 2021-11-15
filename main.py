from tkinter import *
import tkinter

color_window = "#86bbd8"

def translate():
    text = input_text.get()
    toret = ""
    for i in range(0, len(text)):

        
        if i%4==0 and i!=0:
            toret += '\n'
        ascii_text = ord(text[i])
        bin_text = "{0:b}".format(ascii_text)
        print(bin_text) 
        toret += bin_text + ' '
    translated_text.set(toret)

Window = Tk()
Window.config(bg=color_window)
Window.title("Convierte las palabras a binario")
Window.geometry("500x500")
Window.resizable(width=False, height=False)

convert_label = Label(Window,
        text="Introduce la palabra o frase que quieres convertir a binario",
        font='arial 13')
convert_label.config(bg= '#f26419', fg='#000')
convert_label.pack()

input_text = Entry(Window, font="arial 12")
input_text.pack()

botton_translate = Button(Window, text = "Se traduce:",
        font="arial 12",
        command= translate)
botton_translate.config(bg='#f6ae2d', fg='#000', borderwidth=2)
botton_translate.pack()

converted_label = Label(Window,
        text="Resultado de la conversión: ",
        font='arial 12')
converted_label.config(bg= '#f26419', fg='#fff')
converted_label.pack()

translated_text = StringVar()
translated_text.set("")
translated_text_label = Label(Window,
        textvariable=translated_text,
        font="arial 12")
translated_text_label.pack()

Window.mainloop()