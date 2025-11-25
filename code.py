from funciones import mostrar_menu, elección_producto, vuelto, modo_administrador

# Colores de Terminal
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

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
                else:
                    print(f"{VERDE}Compra exitosa. Su cambio es: S/ {cambio}{RESET}\n")
                    vuelto(cambio, stock_bm)
                    print("\n--- Transacción finalizada ---\n")
                    time.sleep(2)
                    ganancias_totales += costo
                    continue
                
            else:
                print(f"{ROJO}Monto insuficiente para la compra.{RESET}")
        
        # Si el usuario selecciona "Salir", producto y costo serán None
        elif producto is None and costo is None:
            print(f"{VERDE}Gracias por usar la máquina expendedora.{RESET}")
            continue
    if dinero_ing == password:
        print(f"{VERDE}Contraseña correcta. Accediendo al modo Administrador ...{RESET}")
        modo_administrador(stock_bm)
        continue
        
    else:
        print(f"{AMARILLO}Has ingresado un monto mayor al permitido.{RESET}")
        continue
