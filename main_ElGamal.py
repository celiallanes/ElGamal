import api_ElGamal


print("  -----------------------------------------------------------------------------------------------------------\n",
      "|                                     Bienvenido a ELGAMAL                                                   |\n",
      " ------------------------------------------------------------------------------------------------------------")
opcion = "x"
while opcion.lower() != "f":
    print("¿Qué operación desea realizar?\n A) Generar claves\n B) Cifrar mensaje\n C) Descifrar mensaje\n D) Firmar "
          "menaje\n E) Verificar firma\n F) Finalizar")
    opcion = input("Pulsa A, B, C, D, E o F: ")
    if opcion.lower() != "a" and opcion.lower() != "b" and opcion.lower() != "c" and opcion.lower() != "d" and opcion.lower() != "e" and opcion.lower() != "f":
        while opcion.lower() != "a" and opcion.lower() != "b" and opcion.lower() != "c" and opcion.lower() != "d" and opcion.lower() != "e" and opcion.lower() != "f":
            print("Opción incorrecta, pruebe de nuevo")
            opcion = input("Pulsa A, B, C, D, E o F: ")

    if opcion.lower() == 'a':
        print("[A: Generar claves] Introduzca...")
        n = input("Número que se asociará a los ficheros generados: ")
        n_bits = input("Número de bits de la clave (Recomentación: 1024 bits): ")
        api_ElGamal.gen_key(n, int(n_bits))

    if opcion.lower() == 'b':
        print("[B: Cifrar] Introduzca...")
        n = input("Número que se asociará a los ficheros generados: ")
        texto_claro = input("Mensaje a cifrar: ")
        pub_key = input("Clave pública del receptor: ")
        c = api_ElGamal.cifrar(n, int(texto_claro), pub_key)

    if opcion.lower() == 'c':
        print("[C: Descifrar] Introduzca...")
        n = input("Número que se asociará a los ficheros generados: ")
        c = input("Mensaje a descifrar :")
        priv_key = input("Clave privada del que descifra: ")
        api_ElGamal.descifrar(n, c, priv_key)

    if opcion.lower() == 'd':
        print("[D: Firmar] Introduzca...")
        n = input("Número que se asociará a los ficheros generados: ")
        msg = input("Mensaje que desee firmar: ")
        priv_key = input("Clave privada del emisor de la firma: ")
        api_ElGamal.firmar(n, msg, priv_key)

    if opcion.lower() == 'e':
        print("[E: Verificar] Introduzca...")
        n = input("Número que se asociará a los ficheros generados: ")
        firma = input("Firma a verificar: ")
        msg = input("Mensaje: ")
        pub_key = input("Clave publica del emisor de la firma: ")
        api_ElGamal.verificar_firma(firma, msg, pub_key)

    print()
    if opcion.lower() != 'f':
        otra_op = input("Pulsa \"+\" si desea realizar otra operación: ")
        if otra_op.lower() != '+':
            opcion = 'f'
