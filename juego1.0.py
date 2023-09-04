import tkinter 
def funcion():
    root2 = tkinter.Tk()
    root2.geometry('500x500')
#generador de frame
root = tkinter.Tk()
root.geometry('500x500')

#generador de boton 
boton = tkinter.Button(root, text="Cual es tu nombre", command=funcion).place(width=100, x=250,y=250)
lb1 = Label( text="Curso",fg="black", bg="ivory").place(x=15,y=50)
root.mainloop()
