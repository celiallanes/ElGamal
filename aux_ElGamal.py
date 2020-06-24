import Crypto.Util.number
import numpy as np




# Obtiene un número primo de n bits: lo ideal es que sea de 1024 bits
from numpy.ma import zeros


def get_prime(n_bits):
    prime = Crypto.Util.number.getPrime(n_bits, randfunc=Crypto.Random.get_random_bytes)
    return prime


def raiz_primitiva(p):
    raicesp = np.zeros(p - 1)
    raiz = False
    aleatorio = 1

    while raiz == False:  # mientras no encuentre la raiz hacer lo siguiente ...
        nosirve = False
        # aleatorio=randint(0,p_a-1)# Varia los numeros de prueva
        aleatorio = aleatorio + 1
        for i in range(1, p):  # varia las potencias de todo el conjunto p
            raicesp[i - 1] = (aleatorio ** i) % p

        # Encontrar raices que sirve
        for j in range(1, len(raicesp)):

            if raicesp[0] == raicesp[j]:  # si algun elemento es igual a otro, no sirve la raiz de prueba
                nosirve = True

            if nosirve == False:  # si despues de evaluar la raiz continua siendo falso nosirve entonces esa raiz es valida
                raiz = True
            else:
                raiz = False

    return raicesp, aleatorio


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
        return  1
    elif b == 1:
        return  a
    elif a == 0:
        return  0
    else:
        result = 1
        z = zeros(b)
        for x in range(b):
            result *= a
        return result

