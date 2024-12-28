from tkinter import *

main = Tk()
main.geometry("1024x630+0+0")
main.resizable(1,1)
main.title("sistema de facturacion")
main.config(bg="violet",)

panel_superior = Frame(main, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

lbl_titulo =Label(panel_superior, text="Sistema de facturacion", fg="azure4", font=("Arial", 58), bg="burlywood", width=27)
lbl_titulo.grid(row=0, column=0)

panel_izquierdo = Frame(main, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4",padx=50)
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19,"bold"))
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",font=("Dosis", 19,"bold"))
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text="Postres",font=("Dosis", 19,"bold"))
panel_postres.pack(side=LEFT)

panel_recibo = Frame(panel_dere)
main.mainloop()