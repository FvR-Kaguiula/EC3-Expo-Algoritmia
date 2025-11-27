from funciones import mostrar_menu, elección_producto, vuelto, modo_administrador
from os import system
# Funciones para fecha/hora en los registros
from time import strftime, localtime

# Código de documentación del módulo

"""
Módulo principal de la máquina expendedora.
    Contiene:
    - inicialización del archivo de registro
    - bucle principal de atención al cliente
    - manejo de modo administrador

    Notas:
    - El módulo importa funciones del archivo `funciones.py` para modularidad.
    - El bucle principal atiende continuamente hasta que el usuario decide salir, luego se reinicia.
    - El modo administrador permite gestionar stock y ver ventas acumuladas.
    - El archivo "registro_maquina_expendedora.txt" es creado y actualizado con cada operación.
        - Cada registro incluye marcas de tiempo, producto vendido, costo, dinero ingresado, cambio devuelto y ganancias totales.
    - El monto máximo permitido para clientes normales es S/100.
"""

# Colores de terminal: utilizados para resaltar mensajes (error/éxito/advertencia)
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

# Inicializar (append) el archivo de registro de operaciones.
# Se usa append para no sobrescribir registros previos.
with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
    archivo_registro.write(f"REGISTRO DE LA MÁQUINA EXPENDEDORA\n")
    archivo_registro.write(f"Fecha de inicio: {strftime('%Y-%m-%d', localtime())}\n")
    archivo_registro.write(f"Hora de inicio: {strftime('%H:%M:%S', localtime())}\n")
    archivo_registro.write("--------------------------------------------------\n")

# Contraseña para entrar al modo administrador (valor numérico)
password = 20122025

# Contador de ganancias acumuladas (se actualiza tras cada venta exitosa)
ganancias_totales = 0.0

# Stock inicial de billetes y monedas: [valor, cantidad]
stock_bm = [
    [50, 5],
    [20, 5],
    [10, 5],
    [5, 5],
    [2, 5],
    [1, 5],
    [0.50, 5],
    [0.20, 5],
    [0.10, 5]
]

# Bucle principal: atención continua hasta terminar el programa
while True:
    import time
    mostrar_menu()

    # Leer monto ingresado por el usuario
    dinero_ing = float(input("Ingrese monto (S/): "))

    # Caso cliente normal: monto permitido hasta S/100
    if dinero_ing <= 100:
        producto, costo = elección_producto()

        # Si el usuario eligió un producto válido (no seleccionó "Salir")
        if producto is not None and costo is not None:
            # Mostrar producto y costo (sin modificar valores)
            print(f"{NEGRITA}Producto seleccionado: {producto}, S/{costo}{RESET}")

            if dinero_ing >= costo:
                # Calcular cambio y redondear a 2 decimales
                cambio = round(dinero_ing - costo, 2)

                if cambio == 0:
                    # Compra exacta, no se devuelve vuelto
                    print(f"{VERDE}Compra exitosa.{RESET}")
                    print("\n--- Transacción finalizada ---\n")

                    # Actualizar ganancias y registrar operación
                    ganancias_totales += costo
                    with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                        hora_actual = strftime("%Y-%m-%d %H:%M:%S", localtime())
                        archivo_registro.write(f"{hora_actual}\n")
                        archivo_registro.write(f"Producto: {producto}\nCosto: S/ {costo}\nDinero ingresado: S/ {dinero_ing}\nCambio devuelto: S/ {cambio}\nGanancias totales: S/ {ganancias_totales}\n")
                        archivo_registro.write("--------------------------------------------------\n")
                    time.sleep(2)
                    continue
                else:
                    # Compra con cambio: delegar desglose a la función `vuelto`
                    print(f"{VERDE}Compra exitosa. Su cambio es: S/ {cambio}{RESET}\n")

                    vuelto(cambio, stock_bm)
                    print("\n--- Transacción finalizada ---\n")

                    ganancias_totales += costo
                    # Registrar la transacción (con timestamp)
                    with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                        hora_actual = strftime("%Y-%m-%d %H:%M:%S", localtime())
                        archivo_registro.write(f"[{hora_actual}]")
                        archivo_registro.write(f"Producto: {producto}\nCosto: S/ {costo}\nDinero ingresado: S/ {dinero_ing}\nCambio devuelto: S/ {cambio}\nGanancias totales: S/ {ganancias_totales}\n")
                        archivo_registro.write("--------------------------------------------------\n")
                    time.sleep(2)
                    continue

            else:
                # Monto insuficiente para comprar el producto
                print(f"{ROJO}Monto insuficiente para la compra.{RESET}")

        # Si el usuario seleccionó la opción 'Salir' desde el menú
        elif producto is None and costo is None:
            print(f"{VERDE}Gracias por usar la máquina expendedora.{RESET}")
            continue

    # Si el usuario ingresó la contraseña exacta, pasar a modo administrador
    if dinero_ing == password:
        print(f"{VERDE}Contraseña correcta. Accediendo al modo Administrador ...{RESET}")
        modo_administrador(stock_bm, ganancias_totales)
        continue

    else:
        # Monto mayor al permitido (fuera de flujo normal de cliente)
        print(f"{AMARILLO}Has ingresado un monto mayor al permitido.{RESET}")
        continue