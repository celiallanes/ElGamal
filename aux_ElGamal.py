import hashlib
import math
import random
import Crypto.Util.number
import numpy as np

folder = 'exports/'
folder_kpub = folder + 'claves/public_'
folder_kpriv = folder + 'claves/private_'
folder_msg = folder + 'mensajes/msg_'
folder_msg_c = folder + 'mensajes_cifrados/msg_cifrado_'
folder_msg_d = folder + 'mensajes_descifrados/msg_descifrado_'
folder_f = folder + 'firmas/signature_'


def get_prime(n_bits):
    prime = Crypto.Util.number.getPrime(n_bits, randfunc=Crypto.Random.get_random_bytes)
    return prime


def raiz_primitiva(p):
    raicesp = np.zeros(p - 1)
    raiz = False
    aleatorio = 1
    while raiz == False:
        nosirve = False
        aleatorio = aleatorio + 1
        for i in range(1, p):
            raicesp[i - 1] = (aleatorio ** i) % p
        for j in range(1, len(raicesp)):
            if raicesp[0] == raicesp[j]:
                nosirve = True
            if nosirve == False:
                raiz = True
            else:
                raiz = False
    return raicesp, aleatorio


def ind_euler(p):
    eulerphi = 0;
    for i in range(1, p):
        if math.gcd(i, p) == 1:
            eulerphi += 1
    return eulerphi


'''
def H_firma(eulerphi, p):
    valido = False
    while valido == False:
        valido = False
        H = random.randint(1, p-2);
        if math.gcd(H, eulerphi) == 1:
            valido = True
    return H
'''


def H_firma(p):
    valido = False
    while valido == False:
        valido = False
        H = random.randint(1, p - 2);
        if math.gcd(H, p - 1) == 1:
            valido = True
    return H


def hash_sha1(msg_fich):
    msg = param_fich(folder + msg_fich)[0]
    msg = bytes(str(msg), 'ISO-8859-1')
    hash_mensaje_md5 = hashlib.md5(msg)
    print("| Hash del documento en md5:", hash_mensaje_md5.hexdigest())
    # hash_base10=int(hash_mensaje_md5.hexdigest(),16)
    # print("Hash en base 10:",hash_base10)

    # separar el hash
    h = hash_mensaje_md5.hexdigest()
    tam_hash = len(h)
    letras = []
    for i in range(0, tam_hash):
        letras.append(h[i])
    # print("tam=", tam_hash)
    # print("Caracteres separados:", letras)

    valordec = []
    val = ''
    for i in range(0, tam_hash):  # de ascii a decimal
        valordec.append(ord(letras[i]))
        val += str(ord(letras[i]))
    return int(val)

    # print("valores decimales del mensaje:",valordec)


def param_fich(fich):
    f = open(fich)
    fich_str = f.read()
    f.close()
    fich_list = fich_str.split(',')
    fich_int = []
    for x in fich_list:
        fich_int.append(int(x))
    return fich_int


def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        result = 1
        for i in range(b):
            result *= a
        return result


def fich_name(n, opcion):
    if opcion.lower() == 'priv_key':
        fich = folder_kpriv + n + '.key'

    if opcion.lower() == 'pub_key':
        fich = folder_kpub + n + '.key'

    if opcion.lower() == 'b':
        fich = folder_msg + n + '.txt'

    if opcion.lower() == 'c':
        fich = folder_msg_c + n + '.pem'

    if opcion.lower() == 'd':
        fich = folder_msg + n + '.txt'

    if opcion.lower() == 'e':
        fich = folder_f + n + '.pem'

    return fich


if __name__ == '__main__':
    x = hash_sha1('msg_5.pem')
    print(x)
