print("#### OPERADORES TERNARIOS ####")

# ressultado = True ? "Verdadero" : "Falso" - si la condicion se cumple, da el primer valor antes de los :. sino, da el segundo. Este formato es en otros lenguajes
a = 10
b = 30

resultado = "a es mayor que b" if a > b else "b es mayor que a"
print(f"Operador ternario: {resultado}")

#Equivalente a lo anterior
#if a > b:
#    resultado = "a es mayor que b"
#else:
#    resultado = "b es mayor que a"