from tkinter import *
import tkinter as tk
"""""
main = Tk()

main.geometry("300x100+500+300")#Tamaño de la ventana y cordenadas dondeaparece

main.resizable(0,0)

main.title("Hola mundo")

main.config(bg="blue")

label = Label(main, text="Hola Mundo")

label.pack(side= TOP) # Etiqueta

exit_buttom = Button(main, text="salir", command=main.quit)

exit_buttom.pack(side=BOTTOM)

main.mainloop()
"""

class VentanaPrincipal:
    def __init__(self,window):
        self.window = window

        window.title("Hola mundo")
        window.geometry("300x100+500+300")
        window.resizable(0,0)
        window.config(bg="blue2")
        self.label = Label(window, text="Hola Mundo")
        self.label.pack(side= TOP) # Etiqueta
        exit_buttom = Button(window, text="salir", command=window.quit)
        exit_buttom.pack(side=BOTTOM)
app = Tk()
my_window=VentanaPrincipal(app)
app.mainloop()