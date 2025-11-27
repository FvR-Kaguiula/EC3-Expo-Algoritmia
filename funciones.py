# Código de colores para la terminal
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

def mostrar_menu():
    print("="*40)
    print(f"{NEGRITA} MÁQUINA EXPENDEDORA{RESET}")
    print("-"*40)
    
    print(f"{NEGRITA}Bebidas{RESET}")
    print(f"{AZUL}1.  Inca Kola 500 ml         - S/ 4.50{RESET}")
    print(f"{AZUL}2.  Coca-Cola 500 ml         - S/ 4.50{RESET}")
    print(f"{AZUL}3.  Agua San Luis 625 ml     - S/ 2.50{RESET}")
    print(f"{AZUL}4.  Agua Cielo 600 ml        - S/ 2.20{RESET}")
    print(f"{AZUL}5.  Frugos Néctar 300 ml     - S/ 3.00{RESET}")
    print(f"{AZUL}6.  Gatorade 500 ml          - S/ 5.00{RESET}")
    print(f"{AZUL}7.  Powerade 500 ml          - S/ 4.80{RESET}")
    print(f"{AZUL}8.  Volt Energética 473 ml   - S/ 4.00{RESET}")
    print(f"{AZUL}9.  Monster 473 ml           - S/ 7.00{RESET}")
    
    print(f"{NEGRITA}Dulces{RESET}")
    print(f"{AZUL}10. Sublime clásico          - S/ 2.00{RESET}")
    print(f"{AZUL}11. Sublime grande           - S/ 3.20{RESET}")
    print(f"{AZUL}12. Triángulo Field          - S/ 1.50{RESET}")
    print(f"{AZUL}13. Chocman                  - S/ 1.50{RESET}")
    print(f"{AZUL}14. Doña Pepa mini           - S/ 2.50{RESET}")
    print(f"{AZUL}15. Wafer Casino             - S/ 1.20{RESET}")
    print(f"{AZUL}16. Oreo pequeño             - S/ 1.80{RESET}")
    print(f"{AZUL}17. Galletas Tentación       - S/ 1.50{RESET}")
    print(f"{AZUL}18. Morochas                 - S/ 1.80{RESET}")
    
    print(f"{NEGRITA}Salado{RESET}")
    print(f"{AZUL}19. Papas Lay’s pequeñas     - S/ 2.50{RESET}")
    print(f"{AZUL}20. Papas Lay’s grandes      - S/ 4.80{RESET}")
    
    print(f"{ROJO}21. Salir{RESET}")
    print("="*40)

productos =[
    ["Inca Kola 500 ml", 4.50],
    ["Coca-Cola 500 ml", 4.50],
    ["Agua San Luis 625 ml", 2.50],
    ["Agua Cielo 600 ml", 2.20],
    ["Frugos Néctar 300 ml", 3.00],
    ["Gatorade 500 ml", 5.00],
    ["Powerade 500 ml", 4.80],
    ["Volt Energética 473 ml", 4.00],
    ["Monster 473 ml", 7.00],
    ["Sublime clásico", 2.00],
    ["Sublime grande", 3.20],
    ["Triángulo Field", 1.50],
    ["Chocman", 1.50],
    ["Doña Pepa mini", 2.50],
    ["Wafer Casino", 1.20],
    ["Oreo pequeño", 1.80],
    ["Galletas Tentación", 1.50],
    ["Morochas", 1.80],
    ["Papas Lay’s pequeñas", 2.50],
    ["Papas Lay’s grandes", 4.80]
]

def elección_producto():
    import time
    while True:
        opcion=int(input(f"{NEGRITA}Elige una opción (1-21): {RESET}"))
        
        if opcion == 21:
            return None, None  # Indica que el usuario desea salir
        
        # Validar si la opción está dentro del rango válido
        indice= opcion - 1
        
        # Módulo de utilidades para la máquina expendedora.

        """
        Contiene:
        - constantes de color para la terminal
        - `mostrar_menu()`          -> muestra el menú de productos
        - `elección_producto()`     -> pide la selección y valida la opción
        - `vuelto()`                -> calcula y desgloza el cambio en billetes/monedas
        - `modo_administrador()`    -> funciones de administración (stock/ventas/reabastecer)

        Notas:
        - El cálculo del vuelto trabaja internamente en centavos (enteros) para evitar
            problemas de precisión con punto flotante.
        """

        if not (0 <= indice < len(productos)):
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        
        producto, costo = productos[indice]
        
        return producto, costo

def vuelto(cambio, stock_bm):
    print(f"{NEGRITA}Desglose de su cambio{RESET}")
    print("-"*30)
    
    while cambio > 0.009:  # Mientras quede cambio por devolver
        for i in range(len(stock_bm)):
            valor, stock = stock_bm[i]                              # Obtener el valor y stock de cada billete/moneda
            if cambio >= valor and stock > 0:                       # Verificar si hay suficiente cambio y stock
                cantidad = round(int(cambio // valor))
                if cantidad > stock:
                    cantidad = stock                                # Ajustar cantidad al stock disponible
                cambio = cambio - cantidad * valor                  # Actualizar el cambio restante
                stock_bm[i][1] -= cantidad
                print(f"{AMARILLO}{'Billetes' if valor >= 1 else 'Monedas'} de S/ {valor:.2f}:{RESET}", cantidad)
    
    if cambio < 0.009:
        print(f"{ROJO}No hay suficiente cambio para devolver S/ {cambio}{RESET}")
        print(f"{ROJO}Por favor, contacte al administrador de la máquina expendedora.{RESET}")
        exit()
    print("-"*30)

def modo_administrador(stock_bm, ganancias_totales=0.0):
    import time
    from time import strftime, localtime
    print(f"{NEGRITA}Bienvenido al modo Administrador.{RESET}")
    # Aquí puedes agregar funcionalidades adicionales para el modo administrador
    print("="*40)
    print("MODO ADMINISTRADOR")
    print("-"*40)
    print(f"{VERDE}Funcionalidades de administrador{RESET}")
    print("1. Ver stock de billetes y monedas")
    print("2. Reabastecer billetes y monedas")
    print("3. Recuento de ventas")
    print("4. Salir del modo Administrador")
    print("5. Terminar programa")
    print("="*40)
    
    # Abrimos el archivo de registro con modo 'a' para agregar información sin borrar lo existente
    while True:
        elec= int(input("Elige una opción (1-5): "))
        if elec == 1:
            print(f"{NEGRITA}Stock actual de billetes y monedas:{RESET}")
            for valor, stock in stock_bm:
                print(f"S/ {valor}: {stock} unidades")
            with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                archivo_registro.write("Se llamó a la función de ver stock de billetes y monedas.\n")
                archivo_registro.write("Fecha y hora de consulta: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
                for valor, stock in stock_bm:
                    archivo_registro.write(f"S/ {valor}: {stock} unidades\n")
                archivo_registro.write("--------------------------------------------------\n")
        elif elec == 2:
            print(f"{NEGRITA}Reabastecer billetes y monedas:{RESET}")
            for i in range(len(stock_bm)):
                valor, stock = stock_bm[i]
                adicional = int(input(f"Ingrese la cantidad a agregar para S/ {valor} (actual: {stock}): "))
                stock_bm[i][1] += adicional
            print(f"{VERDE}Reabastecimiento completado.{RESET}")
            with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                archivo_registro.write("Se llamó a la función de reabastecer billetes y monedas.\n")
                archivo_registro.write("Fecha y hora de reabastecimiento: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
                for valor, stock in stock_bm:
                    archivo_registro.write(f"S/ {valor}: {stock} unidades\n")
                archivo_registro.write("--------------------------------------------------\n")
            continue
        elif elec == 3:
            print(f"{NEGRITA}Recuento de ventas:{RESET}")
            # Aquí puedes implementar la lógica para el recuento de ventas
            print(f"{VERDE}Las ganancias totales son: S/ {ganancias_totales}{RESET}")
            with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                archivo_registro.write("Se llamó a la función de recuento de ventas.\n")
                archivo_registro.write("Fecha y hora de recuento: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
                archivo_registro.write(f"Ganancias totales: S/ {ganancias_totales}\n")
                archivo_registro.write("--------------------------------------------------\n")
        elif elec == 4:
            print(f"{VERDE}Saliendo del modo Administrador...{RESET}")
            break
        elif elec == 5:
            print(f"{ROJO}Terminando programa...{RESET}")
            with open("registro_maquina_expendedora.txt", "a", encoding="utf-8") as archivo_registro:
                archivo_registro.write("El programa fue terminado por el administrador.\n")
                archivo_registro.write("Fecha y hora de terminación: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
                archivo_registro.write("--------------------------------------------------\n\n")
            exit()
# Para quitar las indentaciones de muchas linas de código sin hacerlo una por una
# Seleccionar todo el bloque de código y presionar Shift + Tab
