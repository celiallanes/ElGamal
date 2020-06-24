import random
from math import pow

import Crypto

import aux_ElGamal


folder = 'exports/'


def gen_key(n, n_bits):
    print("------------------------------------------Generando claves------------------------------------------")
    p = aux_ElGamal.get_prime(12)
    alis, a = aux_ElGamal.raiz_primitiva(p)
    ld = random.randint(1, p - 1)  # Debería s.....
    print(str(p))
    print(str(a))
    print(str(ld))
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

    private_key = folder + 'private_' + n + '.key'
    public_key = folder + 'public_' + n + '.key'
    fpriv = open(private_key, 'w')
    fpriv.write(str(priv_key))
    fpriv.close()
    fpub = open(public_key, 'w')
    fpub.write(str(pub_key))
    fpub.close()
    print("\tFicheros \"private_" + n + ".key \" y \"public_" + n + ".key \" generados.")
    print()


def cifrar(n, msg, pub_key_rx):
    pub_key = aux_ElGamal.param_fich(folder + pub_key_rx)
    print(
        "------------------------------------------Cifrando "
        "mensaje------------------------------------------\n\tMensaje: " + str(
            msg) + "\n\tClave publica:" + str(pub_key))
    p, a, b = pub_key
    k = random.randint(1, p - 2)
    c1 = aux_ElGamal.potencia(a, k) % p
    c2 = (aux_ElGamal.potencia(b, k) * msg) % p
    c = [c1, c2]
    print("\tMensaje cifrado: " + str(c))
    print("\t-->C1: " + str(c1))
    print("\t-->C2: " + str(c2))
    print()
    msg_cifrado = folder + 'msg_cifrado_' + n + '.pem'
    f = open(msg_cifrado, "w")
    f.write(str(c1) + "," + str(c2))
    f.close()
    return c


def descifrar(n, c_fich, priv_key_m):
    priv_key = aux_ElGamal.param_fich(folder + priv_key_m)
    c = aux_ElGamal.param_fich(folder + c_fich)
    print(
        "------------------------------------------Descifrando------------------------------------------\n\tMensaje "
        "cifrado: " + str(
            c) + "\n\tClave privada: " + str(priv_key))
    c1, c2 = c
    p, a, ld = priv_key
    c3 = (c1 ** ld) % p
    c4 = Crypto.Util.number.inverse(c3, p)
    msg = (c2 * c4) % p
    print("\tMensaje descifrado: " + str(msg))
    print()
    msg_descifrado = folder + 'msg_descifrado_' + n + '.pem'
    f = open(msg_descifrado, "w")
    f.write(str(msg))
    f.close()
    return msg


# def hash(msg):


if __name__ == '__main__':
    gen_key('1', 1024)
    cifrar('1',99, "public_1.key")
    descifrar('1', "msg_cifrado_1.pem", "private_1.key")
