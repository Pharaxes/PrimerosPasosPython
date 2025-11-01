import tkinter as tk

#se crea la ventana principal
ventana = tk.Tk()
ventana.title("mi primera ventanacon Tkinter")
ventana.geometry("400x300") #ancho en pixeles

#creamos un label
etiqueta = tk.Label(ventana, text='Hola mundo!', font=('Arial', 20))
etiqueta.pack()

#iniciamos el bucle principal de nuestra ventana
ventana.mainloop()


