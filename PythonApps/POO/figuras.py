import tkinter as tk

ventana = tk.Tk()
ventana.title("Cuadro o rectangulo")

#crear etiqyetas y canpos de entrada

lbl_1 = tk.Label(ventana, text ="lado 1:")
lbl_1.grid(row=0, column=0, padx=5, pady=5)
entry_lado1 = tk.Entry(ventana)
entry_lado1.grid(row=0, column=1, padx=5, pady=5)

lbl_2 = tk.Label(ventana, text="lado2:")
lbl_2.grid(row=1, column=0, padx=5, pady=5 )
entry_lado2 = tk.Entry(ventana)
entry_lado2.grid(row=1, column=1, padx=5, pady=5)

def calcular():
    lado1 = float(entry_lado1.get())
    lado2 = float(entry_lado2.get())

    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    canvas.delete("all")

    if lado1 ==lado2:
        figura.config(text= "es un cuadrado")
        canvas.create_rectangle(50,50,150,150,fill="red")
    else:
        figura.config(text=f"area: {area} perimetro: {perimetro}")
#boton y canvas
boton = tk.Button(ventana, text="calcular ", command=calcular)
boton.grid(row=2, column=0, padx=5, pady=5)
canvas = tk.Canvas(ventana, width=200, height=200)
canvas.grid(row=2, column=1, padx=5, pady=5)
#area y perimetro
figura = tk.Label(ventana,text="")
figura.grid(row=3, column=1, padx=5,pady=5)
resultado = tk.Label(ventana, text="")
resultado.grid(row=4, column=1, padx=5, pady=5)

ventana.mainloop()