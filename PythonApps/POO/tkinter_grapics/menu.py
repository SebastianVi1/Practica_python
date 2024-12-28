from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
main = Tk()
main.title("Calculadora de meses sin intereses")
main.geometry("300x250")
months = {"BANORTE ": 3, "BBVA":6, "CITIBANAMEX":12}
lbl_compra = Label(main, text="Total de la compra")
lbl_compra.pack()
txt_compra = Entry(main)
txt_compra.pack()
lbl_compra = Label(main, text="Selecicona una tarjeta")
lbl_compra.pack()
combo_tarjeta = Combobox(main, values=list(months.keys()))
combo_tarjeta.pack() 
lbl_mensualidad = Label(main,text="Mensualidad")
lbl_mensualidad.pack()
txt_mensualidad = Entry(main)
txt_mensualidad.pack()

def calcualr_msi():
    tarjeta = combo_tarjeta.get()
    msi = months[tarjeta]
    messagebox.shwinfo("Mensaje", f"Tu compra es a {msi} meses sin intereses")
    total = float(txt_compra.get())
    mensualidad =txt_compra/msi
    txt_mensualidad.insert(0,f"$ {round(mensualidad,2)}")

def limpiar():
    txt_compra.deleate(0,END)
    txt_mensualidad.deleate(0,END)
    combo_tarjeta.set("")
main.mainloop()

main.calcualr_msi()
main.limpiar()