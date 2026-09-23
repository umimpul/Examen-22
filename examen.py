# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido: uma sanchez
# Curso:2/2
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.

listas_productos = ("caramelos 10 $, puflitos 20$, chupetines 70$, chicles 5$")
input("nombre y apellido:")

# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.

print("lista_productos:", listas_productos)
print("ingrese el producto que quiera comprar:")
producto_seleccionado = ("caramelos 10 $, puflitos 20$, chupetines 70$, chicles 5$")
producto_seleccionado = input("caramelos 10 $, puflitos 20$, chupetines 70$, chicles 5$")
if producto_seleccionado == "caramelos":
    print("el precio es 10 $")
elif producto_seleccionado == "puflitos":
    print("el precio es 20 $")
elif producto_seleccionado == "chupetines":
    print("el precio es 70 $")
elif producto_seleccionado == "chicles":
    print("el precio es 5 $")
else:
    print("producto no válido")
   
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
