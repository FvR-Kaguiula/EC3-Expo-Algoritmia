
def mostrar_menu():
    print("==============================")
    print(" MÁQUINA EXPENDEDORA")
    print("=============================")
    #Bebidas
    print("1.  Inca Kola 500 ml         - S/ 4.50")
    print("2.  Coca-Cola 500 ml         - S/ 4.50")
    print("3.  Agua San Luis 625 ml     - S/ 2.50")
    print("4.  Agua Cielo 600 ml        - S/ 2.20")
    print("5.  Frugos Néctar 300 ml     - S/ 3.00")
    print("6.  Gatorade 500 ml          - S/ 5.00")
    print("7.  Powerade 500 ml          - S/ 4.80")
    print("8.  Volt Energética 473 ml   - S/ 4.00")
    print("9.  Monster 473 ml           - S/ 7.00")
    #dulces
    print("10. Sublime clásico          - S/ 2.00")
    print("11. Sublime grande           - S/ 3.20")
    print("12. Triángulo Field          - S/ 1.50")
    print("13. Chocman                  - S/ 1.50")
    print("14. Doña Pepa mini           - S/ 2.50")
    print("15. Wafer Casino             - S/ 1.20")
    print("16. Oreo pequeño             - S/ 1.80")
    print("17. Galletas Tentación       - S/ 1.50")
    print("18. Morochas                 - S/ 1.80")
    #salado
    print("19. Papas Lay’s pequeñas     - S/ 2.50")
    print("20. Papas Lay’s grandes      - S/ 4.80")
    #salir
    print("21.Salir")
    print("==============================")


def modo_cliente():
    import time
    while True:
        mostrar_menu()
        opcion = input(" Elige una opción (1-21): ")
        if opcion == "1":
            producto, precio = "Inca Kola 500 ml", 4.50
        elif opcion == "2":
            producto, precio = "Coca-Cola 500 ml", 4.50
        elif opcion == "3":
            producto, precio = "Agua San Luis 625 ml", 2.50
        elif opcion == "4":
            producto, precio = "Agua Cielo 600 ml", 2.20
        elif opcion == "5":
            producto, precio = "Frugos Néctar 300 ml", 3.00
        elif opcion == "6":
            producto, precio = "Gatorade 500 ml", 5.00
        elif opcion == "7":
            producto, precio = "Powerade 500 ml", 4.80
        elif opcion == "8":
            producto, precio = "Volt Energética 473 ml", 4.00
        elif opcion == "9":
            producto, precio = "Monster 473 ml", 7.00
        elif opcion == "10":
            producto, precio = "Sublime clásico", 2.00
        elif opcion == "11":
            producto, precio = "Sublime grande", 3.20
        elif opcion == "12":
            producto, precio = "Triángulo Field", 1.50
        elif opcion == "13":
            producto, precio = "Chocman", 1.50
        elif opcion == "14":
            producto, precio = "Doña Pepa mini", 2.50
        elif opcion == "15":
            producto, precio = "Wafer Casino", 1.20
        elif opcion == "16":
            producto, precio = "Oreo pequeño", 1.80
        elif opcion == "17":
            producto, precio = "Galletas Tentación", 1.50
        elif opcion == "18":
            producto, precio = "Morochas", 1.80
        elif opcion == "19":
            producto, precio = "Papas Lay's pequeñas", 2.50
        elif opcion == "20":
            producto, precio = "Papas Lay's grandes", 4.80
        elif opcion == "21":
            print("Gracias por usar la máquina expendedora")
            time.sleep(2)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        
        print("Has elegido", producto, "Precio: S/", precio)
        monto = float(input("Ingresa el monto: S/ "))
        vuelto = monto - precio
        vuelto = round(vuelto, 2)
        
        print("Su vuelto es: S/", vuelto)
        if vuelto >= 200:
            bm = int(vuelto // 200)
            vuelto = vuelto % 200
            print("billete de 200:", bm)
        if vuelto >= 100:
            bm = int(vuelto // 100)
            vuelto = vuelto % 100
            print("billete de 100:", bm)
        if vuelto >= 50:
            bm = int(vuelto // 50)
            vuelto = vuelto % 50
            print("billete de 50:", bm)
        if vuelto >= 20:
            bm = int(vuelto // 20)
            vuelto = vuelto % 20
            print("billete de 20:", bm)
        if vuelto >= 10:
            bm = int(vuelto // 10)
            vuelto = vuelto % 10
            print("billete de 10:", bm)
        if vuelto >= 5:
            bm = int(vuelto // 5)
            vuelto = vuelto % 5
            print("moneda de 5:", bm)
        if vuelto >= 2:
            bm = int(vuelto // 2)
            vuelto = vuelto % 2
            print("moneda de 2:", bm)
        if vuelto >= 1:
            bm = int(vuelto // 1)
            vuelto = vuelto % 1
            print("monedas de 1:", bm)
        if vuelto >= 0.5:
            bm = int(vuelto // 0.5)
            vuelto = vuelto % 0.5
            print("moneda de 0.5:", bm)
        if vuelto >= 0.2:
            bm = int(vuelto // 0.2)
            vuelto = vuelto % 0.2
            print("moneda de 0.2:", bm)
        if vuelto >= 0.1:
            bm = int(vuelto // 0.1)
            vuelto = vuelto % 0.1
            print("moneda de 0.1:", bm)
        
        if vuelto >= precio:
            vuelto = round(vuelto - precio, 2)
            print("compra exitosa ")
            print(f"Retira tu {producto} y tu vuelto: S/ {vuelto}")
        else:
            print("Saldo insuficiente")
            print(f"Te faltan S/ {round(precio - vuelto, 2)} para comprar {producto}.")
        
        print("\n--- Transacción finalizada ---\n")
        time.sleep(2)