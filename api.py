import random
from math import pow


def param_fich(fich):
    f = open(fich)
    key_str = f.read()

    f.close()
    fich_str = key_str.split(',')
    fich_int = [0]
    for x in fich_str:
        fich_int = fich_int.append(x)
    return fich_int


def gen_key(n):
    print("Generando claves ...")
    p = 17
    a = 3
    ld = 6
    b = int(pow(a, ld) % p)
    priv_key = str(p) + ',' + str(a) + ',' + str(ld)
    pub_key = str(p) + ',' + str(a) + ',' + str(b)
    print("\tParámetros generados:")
    print("\t\tp = " + str(p))
    print("\t\talpha = " + str(a))
    print("\t\tlambda = " + str(ld))
    print("\t\tbetha = " + str(b))
    print("\t\tClave pública = [" + pub_key + "]")
    print("\t\tClave privada = [" + priv_key + "]")

    fpriv = open('private_key_' + n, 'w')
    fpriv.write(str(priv_key))
    fpriv.close()
    fpub = open('public_key_' + n, 'w')
    fpub.write(str(pub_key))
    fpub.close()
    print("\tFicheros \"private_key_" + n + "\" y \"public_key_" + n + "\" generados.")
    print()


def cifrar(n, msg, pub_key_rx):
    pub_key = param_fich(pub_key_rx)
    print("Cifrando ...\n\tMensaje: " + str(msg) + "\n\tClave publica:" + str(pub_key))
    p, a, b = pub_key
    k = 5
    c1 = int(pow(a, k) % p)
    c2 = int((pow(b, k) * msg) % p)
    c = [c1, c2]
    print("\tMensaje cifrado: " + str(c))
    print("\t-->C1: " + str(c1))
    print("\t-->C2: " + str(c2))
    print()
    f = open("mensaje_cifrado_" + n, "w")
    f.write(str(c1) + "," + str(c2))
    f.close()
    return c


def descifrar(n, c_fich, priv_key_m):
    priv_key = param_fich(priv_key_m)
    c = param_fich(c_fich)
    print("Descifrando...\n\tMensaje cifrado: " + str(c) + "\n\tClave privada: " + str(priv_key))
    c1, c2 = c
    p, a, ld = priv_key
    msg = int((pow(c1, p - 1 - ld) * c2) % p)
    print("\tMensaje descifrado: " + str(msg) )
    print()
    f = open("mensaje_descifrado_" + n, "w")
    f.write(str(msg))
    f.close()
    return msg


def param_fich(fich):
    f = open(fich)
    fich_str = f.read()
    f.close()
    fich_list = fich_str.split(',')
    fich_int = []
    for x in fich_list:
        fich_int.append(int(x))
    return fich_int


if __name__ == '__main__':
    gen_key('1')
    cifrar('1', 9, "public_key_1")
    descifrar('1', "mensaje_cifrado_1", "private_key_1")
