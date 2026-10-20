monto_total = 0.0
caja_abierta = True 

while caja_abierta:
    print("Menu")
    print("1.regitro venta")
    print("2.ver total acumulado del dia.")
    print("3.cerrar caja y salir.")

    opcion = int(input("ingrese opcion:"))


    if opcion == 1:
        print("cerrar caja y salir.")
        caja_abierta = False

        print("Registro de venta")
        subtotal_cliente = 0
        registro_de_venta = True

        while registro_de_venta:
          
            precio = input("Ingrese el precio de cada producto: ")
            if precio == ("0") or precio == ("fin"):
               registro_de_venta = False
            else:
               precio = float(precio)        
               subtotal_cliente =subtotal_cliente +  (precio)

        print(" el sub total del cliente es ", subtotal_cliente)

    if(opcion == 2):
        print("CERRAR CAJA Y SALIR.")

        caja_abierta = False
    if(opcion == 3):
        print("CERRAR CAJA Y SALIR.")
        caja_abierta = False


        print("---Boleta---")
        print("subtotal: ",subtotal_cliente)
        monto_iva = subtotal_cliente * = 0.19
        total_iva_cliente = subtotal_cliente + monto_iva
        print("Monto IVA: ", monto_iva)
        print("total cliente (+IVA): ", total_iva_cliente)


        input("Presione cualquier tecla para continuar...")
        print("--- Metodo de pago ---")
        metodo_pago = input("1.Efectivo\n2.Tarjeta\nOpción: ")
        descuento = 0.0
        if metodo_pago == "1":
            descuento = total_iva_cliente*0.05
            print("Descuento = 

