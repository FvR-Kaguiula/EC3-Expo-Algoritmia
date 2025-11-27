from funciones import mostrar_menu, elección_producto, vuelto, modo_administrador
from os import system
# Añadir al archivo de registro la hora de cada transacción
from time import strftime, localtime

# Colores de Terminal
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

# Inicializar el archivo de registro con utf-8
with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
    archivo_registro.write(f"REGISTRO DE LA MÁQUINA EXPENDEDORA\n")
    archivo_registro.write(f"Fecha de inicio: {strftime('%Y-%m-%d', localtime())}\n")
    archivo_registro.write(f"Hora de inicio: {strftime('%H:%M:%S', localtime())}\n")
    archivo_registro.write("--------------------------------------------------\n")

password = 20122025
ganancias_totales = 0.0

stock_bm=[
        [50 , 5],
        [20 , 5],
        [10 , 5],
        [5  , 5],
        [2  , 5],
        [1  , 5],
        [0.50 , 5],
        [0.20 , 5],
        [0.10 , 5]
    ]

while True:
    import time
    mostrar_menu()
    
    dinero_ing= float(input("Ingrese monto (S/): "))
    if dinero_ing <= 100:
        producto, costo = elección_producto()
        
        if producto is not None and costo is not None:
            print(f"{NEGRITA}Producto seleccionado: {producto}, S/{costo}{RESET}")
            
            if dinero_ing >= costo:
                cambio = round(dinero_ing - costo, 2) # Round redondear a 2 decimales la operación "dinero_ing - costo"
                
                if cambio == 0:
                    print(f"{VERDE}Compra exitosa.{RESET}")
                    print("\n--- Transacción finalizada ---\n")
                    
                    ganancias_totales += costo
                    # Registrar la transacción en el archivo de registro en cada linea
                    with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                        hora_actual = strftime("%Y-%m-%d %H:%M:%S", localtime())
                        archivo_registro.write(f"{hora_actual}\n")
                        archivo_registro.write(f"Producto: {producto}\nCosto: S/ {costo}\nDinero ingresado: S/ {dinero_ing}\nCambio devuelto: S/ {cambio}\nGanancias totales: S/ {ganancias_totales}\n")
                        archivo_registro.write("--------------------------------------------------\n")
                    time.sleep(2)
                    continue
                else:
                    print(f"{VERDE}Compra exitosa. Su cambio es: S/ {cambio}{RESET}\n")
                    
                    vuelto(cambio, stock_bm)
                    print("\n--- Transacción finalizada ---\n")
                    
                    ganancias_totales += costo
                    # Registrar la transacción en el archivo de registro en cada linea
                    with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                        hora_actual = strftime("%Y-%m-%d %H:%M:%S", localtime())
                        archivo_registro.write(f"[{hora_actual}]")
                        archivo_registro.write(f"Producto: {producto}\nCosto: S/ {costo}\nDinero ingresado: S/ {dinero_ing}\nCambio devuelto: S/ {cambio}\nGanancias totales: S/ {ganancias_totales}\n")
                        archivo_registro.write("--------------------------------------------------\n")
                    time.sleep(2)
                    continue
                
            else:
                print(f"{ROJO}Monto insuficiente para la compra.{RESET}")
        
        # Si el usuario selecciona "Salir", producto y costo serán None
        elif producto is None and costo is None:
            print(f"{VERDE}Gracias por usar la máquina expendedora.{RESET}")
            continue
    if dinero_ing == password:
        print(f"{VERDE}Contraseña correcta. Accediendo al modo Administrador ...{RESET}")
        modo_administrador(stock_bm, ganancias_totales)
        continue
        
    else:
        print(f"{AMARILLO}Has ingresado un monto mayor al permitido.{RESET}")
        continue