import datos


def imprimir_calzado(calzado):
    print(
        f"ID: {calzado.id} | "
        f"Modelo: {calzado.modelo} | "
        f"Talla: {calzado.talla} | "
        f"Precio: ${calzado.precio:.2f}"
    )


def main():
    datos.iniciar_bd()

    while True:
        print("\n===== INVENTARIO DE CALZADO =====")
        print("1. Registrar calzado")
        print("2. Ver inventario")
        print("3. Buscar calzado por ID")
        print("4. Modificar precio")
        print("5. Eliminar calzado")
        print("6. Salir")

        opcion = input("Elija una opción: ").strip()

        try:
            if opcion == "1":
                modelo = input("Modelo: ").strip()
                talla = int(input("Talla: "))
                precio = float(input("Precio: "))

                if not modelo or talla <= 0 or precio <= 0:
                    print("Datos no válidos.")
                    continue

                if datos.registrar_calzado(modelo, talla, precio):
                    print("Calzado registrado correctamente.")
                else:
                    print("No se pudo registrar.")

            elif opcion == "2":
                calzados = datos.obtener_calzados()

                if not calzados:
                    print("No hay calzados registrados.")
                else:
                    for calzado in calzados:
                        imprimir_calzado(calzado)

            elif opcion == "3":
                id_calzado = int(input("ID del calzado: "))
                calzado = datos.obtener_calzado(id_calzado)

                if calzado is None:
                    print("Calzado no encontrado.")
                else:
                    imprimir_calzado(calzado)

            elif opcion == "4":
                id_calzado = int(input("ID del calzado: "))
                precio = float(input("Nuevo precio: "))

                if precio <= 0:
                    print("El precio debe ser mayor que cero.")
                    continue

                if datos.modificar_precio(id_calzado, precio):
                    print("Precio modificado.")
                else:
                    print("Calzado no encontrado.")

            elif opcion == "5":
                id_calzado = int(input("ID del calzado: "))

                if datos.borrar_calzado(id_calzado):
                    print("Calzado eliminado.")
                else:
                    print("Calzado no encontrado.")

            elif opcion == "6":
                print("Hasta pronto.")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()
