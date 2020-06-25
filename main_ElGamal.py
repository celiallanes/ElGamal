import api_ElGamal
from aux_ElGamal import fich_name

print("  ----------------------------------------------\n",
      "|             Bienvenido a ELGAMAL               |\n",
      "  ----------------------------------------------")
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
        print("[A: Generar claves] Introduzca número/letra asociado a...")
        n = input("\tLos ficheros que se generarán: ")
        n_bits = input("\tNúmero de bits de la clave (máx 12, ideal 1024): ")
        api_ElGamal.gen_key(n, int(n_bits))

    if opcion.lower() == 'b':
        error = 1
        print("[B: Cifrar] Introduzca número/letra asociado a...")
        n = input("\tLos ficheros que se generarán: ")
        n_pub_key = input("\tClave pública del receptor: ")
        pub_key = fich_name(n_pub_key, 'pub_key')
        while error:
            n_msg = input("\tMensaje a cifrar: ")
            msg = fich_name(n_msg, opcion.lower())
            error, p = api_ElGamal.cifrar(n, msg, pub_key)
            if error:
                print("\t[CUIDADO]: el mensaje debe ser menor que p (p=" + str(p) + ").")

    if opcion.lower() == 'c':
        print("[C: Descifrar] Introduzca número/letra asociado a...")
        n = input("\tLos ficheros que se generarán: ")
        n_c = input("\tMensaje a descifrar: ")
        c = fich_name(n_c, opcion)
        n_priv_key = input("\tClave privada del que descifra: ")
        priv_key = fich_name(n_priv_key, 'priv_key')
        api_ElGamal.descifrar(n, c, priv_key)

    if opcion.lower() == 'd':
        print("[D: Firmar] Introduzca número/letra asociado a...")
        n = input("\tFicheros generados: ")
        n_msg = input("\tMensaje que desee firmar: ")
        msg = fich_name(n_msg, opcion)
        n_priv_key = input("\tClave privada del emisor de la firma: ")
        priv_key = fich_name(n_priv_key, 'priv_key')
        api_ElGamal.firmar(n, msg, priv_key)

    if opcion.lower() == 'e':
        print("[E: Verificar] Introduzca número/letra asociado a...")
        n = input("\tFicheros generados: ")
        n_firma = input("\tFirma a verificar: ")
        firma = fich_name(n_firma, opcion)
        n_msg = input("\tMensaje: ")
        msg = fich_name(n_msg, 'b')
        n_pub_key = input("\tClave pública del emisor de la firma: ")
        pub_key = fich_name(n_pub_key, 'pub_key')
        api_ElGamal.verificar_firma(firma, msg, pub_key)

    print()
    if opcion.lower() != 'f':
        otra_op = input("Pulsa \"+\" si desea realizar otra operación: ")
        print()
        if otra_op.lower() != '+':
            opcion = 'f'
