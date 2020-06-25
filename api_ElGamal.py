import random
import Crypto
from Crypto.Util.number import inverse
import aux_ElGamal

def gen_key(n, n_bits):
    print("-----------------------Generando claves-----------------------")
    p = aux_ElGamal.get_prime(n_bits)
    alis, a = aux_ElGamal.raiz_primitiva(p)
    ld = random.randint(1, p - 1)  # Debería s.....
    b = (aux_ElGamal.potencia(a, ld) % p)
    priv_key = str(p) + ',' + str(a) + ',' + str(ld)
    pub_key = str(p) + ',' + str(a) + ',' + str(b)
    print("\tParámetros generados:")
    print("\t\tp = " + str(p))
    print("\t\talpha = " + str(a))
    print("\t\tlambda = " + str(ld))
    print("\t\tbetha = " + str(b))
    print("\t\tClave pública = [" + pub_key + "]")
    print("\t\tClave privada = [" + priv_key + "]")
    print()
    private_key = aux_ElGamal.folder_kpriv + n + '.key'
    public_key = aux_ElGamal.folder_kpub + n + '.key'
    fpriv = open(private_key, 'w')
    fpriv.write(str(priv_key))
    fpriv.close()
    fpub = open(public_key, 'w')
    fpub.write(str(pub_key))
    fpub.close()
    print("\tFichero \"" + public_key + " \" generado.")
    print("\tFichero \"" + private_key + " \" generado.")
    print("----------------------------------------------\n")


def cifrar(n, msg_fich, pub_key_rx):
    error = 0
    msg = aux_ElGamal.param_fich(msg_fich)[0]
    pub_key = aux_ElGamal.param_fich(pub_key_rx)
    p, a, b = pub_key
    if msg >= p:
        error = 1
    else:
        print("-----------------------Cifrando mensaje-----------------------\n\tMensaje: " + str(msg) + "\n\tClave publica:" + str(pub_key))
        k = random.randint(1, p - 2)
        c1 = aux_ElGamal.potencia(a, k) % p
        c2 = (aux_ElGamal.potencia(b, k) * msg) % p
        c = [c1, c2]
        print("\tk: " + str(k))
        print("\tMensaje cifrado: " + str(c))
        print("\t-->C1: " + str(c1))
        print("\t-->C2: " + str(c2))
        print()
        msg_cifrado = aux_ElGamal.folder_msg_c + n + '.pem'
        f = open(msg_cifrado, "w")
        f.write(str(c1) + "," + str(c2))
        f.close()
        print("\tFichero \"" + msg_cifrado + "\" generado.")
        print("----------------------------------------------\n")
    return error, p


def descifrar(n, c_fich, priv_key_m):
    priv_key = aux_ElGamal.param_fich(priv_key_m)
    c = aux_ElGamal.param_fich(c_fich)
    print("-----------------------Descifrando"
          "-----------------------\n\tMensaje "
          "cifrado: " + str(c) + "\n\tClave privada: " + str(priv_key))
    c1, c2 = c
    p, a, ld = priv_key
    c3 = aux_ElGamal.potencia(c1, ld) % p
    c4 = Crypto.Util.number.inverse(c3, p)
    msg = (c2 * c4) % p
    print("\tMensaje descifrado: " + str(msg))
    print()
    msg_descifrado = aux_ElGamal.folder_msg_d + n + '.pem'
    f = open(msg_descifrado, "w")
    f.write(str(msg))
    f.close()
    print("\tFichero \"" + msg_descifrado + "\" generado.")
    print("----------------------------------------------\n")
    return msg


def firmar(n, msg_fich, priv_key_m):
    priv_key = aux_ElGamal.param_fich(priv_key_m)
    msg = aux_ElGamal.param_fich(msg_fich)[0]
    print("-----------------------Firmando"
          "-----------------------\n\tMensaje "
          ": " + str(msg) + "\n\tClave privada: " + str(priv_key))
    p, a, ld = priv_key
    # euler_phi = aux_ElGamal.ind_euler(p)
    # H = aux_ElGamal.H_firma(euler_phi, p)
    # H_inv = inverse(H, euler_phi)
    # r = aux_ElGamal.potencia(a, H) % (p-1)
    # s = ((h_msg - ld * r) * H_inv) % euler_phi
    H = aux_ElGamal.H_firma(p)
    H_inv = inverse(H, p - 1)
    r = aux_ElGamal.potencia(a, H) % p
    s = (H_inv * (msg - ld * r)) % (p - 1)
    firma = [r, s]
    print("\tMensaje: " + str(msg))
    print("\tFirma digital: " + str(firma))
    print("\t-->r: " + str(r))
    print("\t-->s: " + str(s))
    print()
    firma_digital = aux_ElGamal.folder_f + n + '.pem'
    f = open(firma_digital, "w")
    f.write(str(r) + "," + str(s))
    f.close()
    print("\tFichero \"" + firma_digital + "\" generado.")
    print("----------------------------------------------\n")


def verificar_firma(firma_fich, msg_fich, public_key_e):
    public_key = aux_ElGamal.param_fich(public_key_e)
    firma = aux_ElGamal.param_fich(firma_fich)
    msg = aux_ElGamal.param_fich(msg_fich)[0]
    print("-----------------------Verificando "
          "firma-----------------------\n\tMensaje: " + str(msg) + "\n\tFirma: " + str(firma) +
          "\n\tClave pública: " + str(public_key))
    p, a, b = public_key
    r, s = firma
    if r < 1 or r > p - 1: return False
    n1 = aux_ElGamal.potencia(b, r) % p
    n2 = aux_ElGamal.potencia(r, s) % p
    k = (n1 * n2) % p
    verificacion = aux_ElGamal.potencia(a, msg) % p
    if verificacion == k:
        print("\tVerificación completada: firma VÁLIDA.")
    else:
        print("\tVerificación completada: firma NO VÁLIDA.")
    print("----------------------------------------------\n")


if __name__ == '__main__':
    gen_key('1', 1024)
    cifrar('1', 99, "public_1.key")
    descifrar('1', "msg_cifrado_1.pem", "private_1.key")
    firmar('1', 'msg_5.pem', 'private_1.key')
    verificar_firma('signature_1.pem', 'msg_5.pem', 'public_1.key')
