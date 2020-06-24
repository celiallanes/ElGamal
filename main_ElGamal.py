import api_ElGamal

opcion = "x"
while opcion.lower() != "d":
    print(
        "¿Qué operación desea realizar?\n A) Generar claves\n B) Enviar mensaje crifrado\n C) Recibir mensaje y descifrarlo\n D) Finalizar")
    opcion = input("Pulsa A, B, C o D: ")
    if opcion.lower() != "a" and opcion.lower() != "b" and opcion.lower() != "c" and opcion.lower() != "d":
        while opcion.lower() != "a" and opcion.lower() != "b" and opcion.lower() != "c" and opcion.lower() != "d":
            print("Opción incorrecta, pruebe de nuevo")
            opcion = input("Pulsa A, B, C o D: ")

    if opcion.lower() == 'a':
        n = input("Introduzca el número que se asociará a los ficheros generados: ")
        n_bits = input("Introduxca el número de bits de la clave (Recomentación: 1024 bits): ")
        api_ElGamal.gen_key(n, int(n_bits))

    if opcion.lower() == 'b':
        n = input("Introduzca el número que se asociará a los ficheros generados: ")
        texto_claro = input("Introduzca el mensaje que desee cifrar: ")
        pub_key = input("Introduzca la clave pública del receptor (p, alpha, betha): ")
        c = api_ElGamal.cifrar(n, int(texto_claro), pub_key)

    if opcion.lower() == 'c':
        n = input("Introduzca el número que se asociará a los ficheros generados: ")
        c = input("Introduzca el nombre del fichero con el mensaje descifrar :")
        priv_key = input("Introduzca su clave privada(p, alpha, lambda): ")
        api_ElGamal.descifrar(n, c, priv_key)

    print()
    if opcion.lower() != 'd':
        otra_op = input("Pulsa \"+\" si desea realizar otra operación: ")
        if otra_op.lower() != '+':
            opcion = 'd'