from mascota_virtual import MascotaVirtual

class TestMascotaVirtual:
    
    @staticmethod
    def test():
        mascota = MascotaVirtual("Panda")
        print(f"Tu mascota se llama {mascota.obtenerNombre()}")

        while True:
            print("1. COMANDOS\n2. CONSULTAS.\n3. ESTADO DE TU MASCOTA.\n4. SALIR.\n")
            opcionprincipal = int(input("> "))

            if opcionprincipal == 1:
                while True:
                    print("1. COMER\n2. BEBER\n3. DORMIR\n4. DESPERTAR\n5. JUGAR\n6. CAMINAR\n7. SALTAR\n8. BAÑAR\n9. VOLVER AL MENU\n")
                    opcion = int(input("> "))

                    if opcion == 9:
                        break

                    if opcion == 1:
                        mascota.comer()
                        print("La mascota se alimentó correctamente.")
                    elif opcion == 2:
                        mascota.beber()
                        print("La mascota bebió correctamente.")
                    elif opcion == 3:
                        mascota.dormir()
                        print("La mascota durmió correctamente.")
                    elif opcion == 4:
                        mascota.despertar()
                        print("La mascota se despertó correctamente.")
                    elif opcion == 5:
                        mascota.jugar()
                        print("La mascota jugó correctamente.")
                    elif opcion == 6:
                        mascota.caminar()
                        print("La mascota caminó correctamente.")
                    elif opcion == 7:
                        mascota.saltar()
                        print("La mascota saltó correctamente.")
                    elif opcion == 8:
                        mascota.bañar()
                        print("La mascota se bañó correctamente.")
                    else:
                        print("Opción incorrecta, intenta de nuevo.")

            elif opcionprincipal == 4:
                print("Juego apagado")
                return
            
            else:
                print("Opción inválida, intenta de nuevo.")



if __name__ == '__main__':
    TestMascotaVirtual.test()