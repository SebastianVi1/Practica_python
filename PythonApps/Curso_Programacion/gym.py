from tkinter import *
from tkinter.ttk import *
main = Tk()
main.geometry("800x600")
def openSelector():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(main)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("800x600")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    btnSalir = Button(newWindow,text="Regresar",command=newWindow.quit)
    btnSalir.pack(side=BOTTOM)
    
    Etiqueta_pecho = Frame(newWindow, bd=5,side=TOP)
    Etiqueta_pecho.grid()
    
btnInicio = Button(main,text="Inicio",command=openSelector,)
btnInicio.grid(row=1,column=0,padx=350,pady=280)


#exitButtom = Button(main, text="salir", command=main.quit)

#exitButtom.grid()

main.mainloop()