from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk

main = Tk()
main.title("Presupuesto anual")
main.geometry("300x250")
main.resizable(1,1)
main.config(bg="red")
areas ={"Ginecologia ": .40,"Traumatologia":.25,"Pediatria":.30,"Investigacion":.5}


ginecologia = Label(main, text="Escoje el area a determinar")
ginecologia.pack()
area1 = Combobox(main, values=list(areas.keys()))
area1.pack() 
asd = Label(main, text="Coloque una cantidad")
asd.pack()
entry1= Entry(main, text= "Coloca la cantidad")
entry1.pack()


def calcular():
    area22= area1.get()
    msi = areas[area22]
    total = float(entry1.get()) * msi
    messagebox.showinfo("Mensaje", f"El total seria de {total}$ ")

boton = tk.Button(main, text="calcular ", command=calcular)
boton.pack()
        

def limpiar():
    entry1.delete(0,END)
    area1.set("")

exit = Button(main, text="Salir",command=main.destroy)
exit.pack()

limpiar = tk.Button(main, text="Limpiar", command=limpiar)
limpiar.pack()
main.mainloop()
main.calcular()
main.limpiar()
