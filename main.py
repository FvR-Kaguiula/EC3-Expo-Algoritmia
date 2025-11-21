from funciones import mostrar_menu, elección_producto, vuelto, modo_administrador
import time

# Colores de Terminal
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

password = 20122025

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
    mostrar_menu()
    time.sleep(0.18)  # pequeña pausa después de mostrar el menú para que se lea con calma
    
    dinero_ing= float(input("Ingrese monto (S/): "))
    if dinero_ing <= 100:
        producto, costo = elección_producto()
        time.sleep(0.12)
        
        if producto is not None and costo is not None:
            print(f"{NEGRITA}Producto seleccionado: {producto}, S/{costo}{RESET}")
            time.sleep(0.16)
            
            if dinero_ing >= costo:
                cambio = round(dinero_ing - costo, 2)
                
                if cambio == 0:
                    print(f"{VERDE}Compra exitosa.{RESET}")
                    time.sleep(0.14)
                    print("\n--- Transacción finalizada ---\n")
                    time.sleep(0.18)
                else:
                    print(f"{VERDE}Compra exitosa. Su cambio es: S/ {cambio}{RESET}\n")
                    time.sleep(0.12)
                    vuelto(cambio, stock_bm)
                    time.sleep(0.18)
                    print("\n--- Transacción finalizada ---\n")
                    time.sleep(0.18)
                    continue
                
            else:
                print(f"{ROJO}Monto insuficiente para la compra.{RESET}")
                time.sleep(0.18)
        
        # Si el usuario selecciona "Salir", producto y costo serán None
        elif producto is None and costo is None:
            print(f"{VERDE}Gracias por usar la máquina expendedora.{RESET}")
            time.sleep(0.14)
            continue
    if dinero_ing == password:
        print(f"{VERDE}Contraseña correcta. Accediendo al modo Administrador ...\n{RESET}")
        time.sleep(0.25)
        modo_administrador(stock_bm)
        time.sleep(0.12)
        continue
        
    else:
        print(f"{AMARILLO}Has ingresado un monto mayor al permitido.{RESET}")
        time.sleep(0.18)
        continue
