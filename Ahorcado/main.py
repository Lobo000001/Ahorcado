import random

estadisticas = [] 
modo_juego = "clasico"


def mostrar_menu():
        #Menu principal
        print("\n--- MENÚ PRINCIPAL ---")
        print("\n1. Iniciar juego")
        print("2. Configuración")
        print("3. Estadísticas")
        print("4. Salir")
        opcion = input("\nElige una opción: ")
        return opcion.strip()

def configuracion():
        #Configuracion

        global modo_juego

        print("\n\n--- Configuracion ---")
        print("\n1. Modo clasico")
        print("\n2. Modo oxigeno")
        opcion = input("\n\nElije una opción:")
        
        if opcion == "1":
            modo_juego = "clasico"
            print("Modo de juego configurado a 'clásico'.")
        elif opcion == "2":
            modo_juego = "oxigeno"
            print("Modo de juego configurado a 'oxígeno'.")
        else:
            print("Opción inválida, no se cambió el modo.")


def historial_partidas():
        #estadisticas
        if not estadisticas:
            print("\n--- Historial de partidas ---")
            print("\nSin historial")
            input("\n\nPresione enter para salir.")
            return 
 
        cont = 1
        print("--- Historial de partidas ---")
        for partida in estadisticas:
            palabra = partida [0]
            resultado = partida [1]
            print("%d. Palabra: %s, Resultado: %s" % (cont, palabra, resultado) )
            cont += 1
        input("\n\nPresione enter para salir")
        return

def jugar_denuevo():
    #Jugar de nuevo
    while True:
        print("\n1. Jugar de nuevo")
        print("2. Volver al menú principal")
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            return "jugar"
        elif opcion == "2":
            return "menu"
        else:
            print("Opción inválida, intenta de nuevo.")


def jugar():
        #Comienza el juego

        global modo_juego

        palabras = ("python", "ahorcado", "programa", "computadora", "laptop", "musica", "encebollado", "plotter")
        palabra_secreta = random.choice(palabras)
        letras_adivinadas = set()

        intentos = 6
        oxigeno = 100
        perdida = 20

        if modo_juego == "clasico":
            print("\n\nTienes 6 intentos para adivinar la palabra")
        else:
            print("\n\nModo oxígeno activado: tienes 100% de oxígeno.")
            print("Cada error reduce tu oxígeno en %d%%." %(perdida))

        while True:
            estado_palabra = ""
            for letra in palabra_secreta:
                if letra in letras_adivinadas:
                        estado_palabra += letra + " "
                else:
                        estado_palabra += "_ "

            print("\n Palabra:", estado_palabra.strip())
    
            letra_usuario = input("\nIngresa una letra: ").lower().strip()
                    
            if len(letra_usuario) != 1 or not letra_usuario.isalpha():
                print("\nPor favor, ingresa solo una letra válida.")
                continue
            if letra_usuario in letras_adivinadas:
                print("\nYa has adivinado esa letra, prueba con otra.")
                continue
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in palabra_secreta:
                    print("\n¡Bien! La letra está en la palabra.")
                    
            else:
                if modo_juego == "clasico":
                    intentos -= 1
                    print("\nLa letra no está. Te quedan %d intentos." %(intentos))
                    if intentos == 0:
                        print("\n¡Te han colgado! La palabra correcta era: %s" %(palabra_secreta))
                        estadisticas.append((palabra_secreta, "Perdiste"))
                        break
                else:
                    oxigeno -= perdida
                    print("\nLa letra no está. Te quedan %d%% oxigeno." %(oxigeno))
                    if oxigeno <= 0:
                        print("\n¡Te quedaste sin oxigeno! La palabra correcta era: %s" %(palabra_secreta))
                        estadisticas.append((palabra_secreta, "Perdiste"))
                        break
            if all(letra in letras_adivinadas for letra in palabra_secreta):
                        print("\n¡Felicidades! Adivinaste la palabra: %s" %(palabra_secreta))
                        estadisticas.append((palabra_secreta, "Ganaste"))
                        break

        decision = jugar_denuevo()
        if decision == "jugar":
            jugar()  # llamas a jugar otra vez
        elif decision == "menu":
            return  # vuelves al menú principal
            
def main():
        #Función del menu1

        while True:
            opcion = mostrar_menu()

            if opcion == "1":
                jugar()
            elif opcion == "2":
                configuracion()
            elif opcion == "3":
                historial_partidas()
            elif opcion == "4":
                print("Gracias por jugar. ¡Hasta luego!")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
        main()