import tkinter as tk

def saludar():
    print('Hola!')

def despedir():
    print('Chau!')

def disculpa():
    print('Perdon!')

#se crea la ventana principal
ventana = tk.Tk()
ventana.title("Ahora tenemos tres boton")
ventana.geometry("400x200") #ancho en pixeles

#creamos un Boton
boton1 = tk.Button(ventana, text='Boton 1', command=saludar)
boton2 = tk.Button(ventana, text='Boton 2', command=despedir)
boton3 = tk.Button(ventana, text='Boton 3', command=disculpa)


boton1.pack(side="top")
boton2.pack(side="left")
boton3.pack(side="right")

#iniciamos el bucle principal de nuestra ventana
ventana.mainloop()
