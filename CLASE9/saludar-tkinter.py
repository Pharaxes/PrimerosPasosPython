import tkinter as tk

def saludar():
    print('Hola!')

#se crea la ventana principal
ventana = tk.Tk()
ventana.title("Ahora tenemos un boton")
ventana.geometry("400x200") #ancho en pixeles

#creamos un Boton
boton = tk.Button(ventana, text='Saludar', font=('Arial', 20), command=saludar)
boton.pack()

#iniciamos el bucle principal de nuestra ventana
ventana.mainloop()
